---
name: windows_powershell_automation_patterns
description: PowerShell patterns for system monitoring and automated troubleshooting
---

# Skill: Windows PowerShell Automation Patterns

## When to use
When automating system diagnostics, monitoring, or implementing defensive troubleshooting for Windows systems.

## Identity
You are a PowerShell automation expert who creates robust, error-handled scripts that monitor system health and implement intelligent remediation. You focus on practical patterns that work reliably in real environments.

## Core principles

1. **Use try-catch blocks for all external operations** - Network, file, and WMI calls can fail
2. **Log everything with timestamps** - Use `Write-Output "$(Get-Date): Action completed"` pattern
3. **Test prerequisites before actions** - Check if services exist, adapters are present, etc.
4. **Implement gradual escalation** - Try gentle fixes before forceful ones
5. **Use background jobs for long-running monitoring** - `Start-Job` for continuous monitoring
6. **Store baselines for comparison** - Save "good" state to compare against current state
7. **Make scripts resume-safe** - Check current state before applying changes
8. **Use structured output** - Return objects, not just strings, for pipeline compatibility
9. **Implement timeout mechanisms** - Don't let scripts hang indefinitely
10. **Validate admin rights when needed** - Check `([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] 'Administrator')`

## Common mistakes

1. Not handling network adapter name variations (Wi-Fi vs WiFi vs Wireless)
2. Assuming WMI/CIM queries will always return results
3. Running restart commands without checking current state first
4. Not implementing delays between related operations (disable/enable cycles)
5. Forgetting that some cmdlets require elevation

## Quality check

1. Does the script check prerequisites before attempting actions?
2. Are all external calls wrapped in error handling?
3. Does it log both successes and failures with context?
4. Can it run multiple times safely without side effects?
5. Does it provide actionable output for both automated and human consumption?

## Automation Patterns

### Network Interface Monitoring & Recovery

```powershell
# Network adapter restart with validation
function Restart-NetworkAdapter {
    param([string]$AdapterName = "Wi-Fi")

    try {
        $adapter = Get-NetAdapter -Name $AdapterName -ErrorAction Stop
        if ($adapter.Status -eq "Up") {
            Write-Output "$(Get-Date): Restarting adapter $AdapterName"
            Restart-NetAdapter -Name $AdapterName -Confirm:$false
            Start-Sleep -Seconds 5

            $newStatus = (Get-NetAdapter -Name $AdapterName).Status
            Write-Output "$(Get-Date): Adapter status after restart: $newStatus"
            return $newStatus -eq "Up"
        } else {
            Write-Output "$(Get-Date): Adapter $AdapterName already down"
            return $false
        }
    } catch {
        Write-Error "$(Get-Date): Failed to restart adapter: $_"
        return $false
    }
}
```

### Event Log Monitoring with Alerts

```powershell
# Monitor for specific events and take action
function Monitor-SystemEvents {
    param(
        [int[]]$EventIDs = @(41, 1074),  # Unexpected/planned shutdowns
        [int]$HoursBack = 1
    )

    $startTime = (Get-Date).AddHours(-$HoursBack)

    try {
        $events = Get-WinEvent -FilterHashtable @{
            LogName = 'System'
            ID = $EventIDs
            StartTime = $startTime
        } -ErrorAction Stop

        foreach ($event in $events) {
            $message = "$(Get-Date): Event $($event.Id) at $($event.TimeCreated): $($event.LevelDisplayName)"
            Write-Output $message

            # Take specific actions based on event type
            switch ($event.Id) {
                41 { Write-Warning "Unexpected shutdown detected - check power supply" }
                1074 { Write-Output "Planned shutdown recorded" }
            }
        }

        return $events.Count
    } catch [System.Exception] {
        if ($_.Exception.Message -match "No events were found") {
            Write-Output "$(Get-Date): No matching events found"
            return 0
        } else {
            Write-Error "$(Get-Date): Error querying events: $_"
            return -1
        }
    }
}
```

### Performance Baseline Collection

```powershell
# Collect performance baseline for later comparison
function Collect-PerformanceBaseline {
    param([string]$OutputPath = "baseline-$(Get-Date -Format 'yyyy-MM-dd-HHmm').csv")

    try {
        $metrics = @()

        # CPU Usage
        $cpu = Get-Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 5
        $avgCpu = ($cpu.CounterSamples | Measure-Object CookedValue -Average).Average

        # Memory Usage
        $memory = Get-WmiObject -Class Win32_OperatingSystem
        $memoryUsagePercent = [math]::Round(((($memory.TotalVisibleMemorySize - $memory.FreePhysicalMemory) / $memory.TotalVisibleMemorySize) * 100), 2)

        # Disk Usage
        $disk = Get-WmiObject -Class Win32_LogicalDisk | Where-Object {$_.DriveType -eq 3}

        $baseline = [PSCustomObject]@{
            Timestamp = Get-Date
            CPUPercent = [math]::Round($avgCpu, 2)
            MemoryPercent = $memoryUsagePercent
            DiskFreeGB = [math]::Round(($disk | Measure-Object FreeSpace -Sum).Sum / 1GB, 2)
            ProcessCount = (Get-Process).Count
        }

        $baseline | Export-Csv -Path $OutputPath -NoTypeInformation -Append
        Write-Output "$(Get-Date): Baseline collected to $OutputPath"
        return $baseline

    } catch {
        Write-Error "$(Get-Date): Failed to collect baseline: $_"
        return $null
    }
}
```

### Driver Status Monitoring

```powershell
# Check for driver issues
function Get-DriverStatus {
    param([string[]]$DeviceClasses = @("Net", "Display", "System"))

    try {
        $problemDevices = @()

        foreach ($class in $DeviceClasses) {
            $devices = Get-WmiObject -Class Win32_SystemDriver | Where-Object {
                $_.State -ne "Running" -and $_.StartMode -ne "Disabled"
            }

            $problemDevices += $devices | Select-Object Name, State, Status, PathName
        }

        if ($problemDevices.Count -gt 0) {
            Write-Warning "$(Get-Date): Found $($problemDevices.Count) driver issues"
            $problemDevices | ForEach-Object {
                Write-Output "Problem: $($_.Name) - State: $($_.State) - Status: $($_.Status)"
            }
        } else {
            Write-Output "$(Get-Date): All monitored drivers running normally"
        }

        return $problemDevices

    } catch {
        Write-Error "$(Get-Date): Failed to check driver status: $_"
        return @()
    }
}
```

### File System Monitoring

```powershell
# Monitor directory for changes
function Start-DirectoryMonitor {
    param(
        [string]$Path,
        [string[]]$Filter = @("*.*"),
        [System.IO.NotifyFilters]$NotifyFilter = [System.IO.NotifyFilters]::All
    )

    try {
        $watcher = New-Object System.IO.FileSystemWatcher
        $watcher.Path = $Path
        $watcher.Filter = $Filter[0]  # FileSystemWatcher takes single filter
        $watcher.NotifyFilter = $NotifyFilter
        $watcher.EnableRaisingEvents = $true

        # Event handlers
        $action = {
            $path = $Event.SourceEventArgs.FullPath
            $name = $Event.SourceEventArgs.Name
            $changeType = $Event.SourceEventArgs.ChangeType
            $timestamp = Get-Date

            Write-Output "$timestamp: File $name $changeType in $path"
        }

        Register-ObjectEvent -InputObject $watcher -EventName "Created" -Action $action
        Register-ObjectEvent -InputObject $watcher -EventName "Changed" -Action $action
        Register-ObjectEvent -InputObject $watcher -EventName "Deleted" -Action $action
        Register-ObjectEvent -InputObject $watcher -EventName "Renamed" -Action $action

        Write-Output "$(Get-Date): Started monitoring $Path"
        return $watcher

    } catch {
        Write-Error "$(Get-Date): Failed to start directory monitor: $_"
        return $null
    }
}
```

## What's Achievable vs Human Intervention

**✅ Fully Automatable:**
- Network adapter restart cycles
- Service restart and monitoring
- Performance data collection and trending
- Event log parsing and alerting
- File system monitoring and basic remediation
- Process monitoring and resource cleanup

**⚠️ Partially Automatable:**
- Driver updates (can detect, installation needs approval)
- Network profile switching (can detect issues, may need credentials)
- Windows Update management (can check, installation timing varies)

**❌ Requires Human Intervention:**
- Hardware replacement decisions
- Network security configuration changes
- System restore/recovery operations
- BIOS/UEFI modifications