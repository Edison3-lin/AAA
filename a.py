#!/usr/bin/env python 
# -*- coding: utf- -*- 
#http://www.cnblogs.com/liu-ke/
import wmi 
import os 
import sys 
import platform 
import time 

def sys_version(): 
    c = wmi.WMI () 
    #獲取作業系統版本 
    for sys in c.Win_OperatingSystem():
        print("Version:%s" % sys.Caption.encode("UTF"),"Vernum:%s" % sys.BuildNumber) 
        print(sys.OSArchitecture.encode("UTF")) #系統是位還是位的 
        print(sys.NumberOfProcesses)            #當前系統執行的程序總數
    
def cpu_mem(): 
    c = wmi.WMI ()    
    #CPU型別和記憶體 
    for processor in c.Win_Processor(): 
        #print "Processor ID: %s" % processor.DeviceID 
        print("Process Name: %s" % processor.Name.strip()) 
    for Memory in c.Win_PhysicalMemory(): 
        print("Memory Capacity: %.fMB" % (int(Memory.Capacity))) 
    
def disk(): 
    c = wmi.WMI ()  
    #獲取硬碟分割槽 
    for physical_disk in c.Win_DiskDrive (): 
        for partition in physical_disk.associators("Win_DiskDriveToDiskPartition"): 
            for logical_disk in partition.associators("Win_LogicalDiskToPartition"): 
                print(physical_disk.Caption.encode("UTF"), partition.Caption.encode("UTF"), logical_disk.Caption) 
    #獲取硬碟使用百分情況 
    for disk in c.Win_LogicalDisk (DriveType): 
        print(disk.Caption, "%.f%% free" % (long (disk.FreeSpace) / long (disk.Size))) 
    
def network(): 
    c = wmi.WMI()
    #獲取MAC和IP地址 
    for interface in c.Win_NetworkAdapterConfiguration (IPEnabled): 
        print("MAC: %s" % interface.MACAddress) 
    for ip_address in interface.IPAddress: 
        print("ip_add: %s" % ip_address) 
    
def main(): 
    sys_version() 
    cpu_mem() 
    disk() 
    network() 

# print(platform.system()) 
# print(platform.release()) 
# print(platform.version()) 
# print(platform.platform()) 
# print(platform.machine())


if __name__ == '__main__': 
    main() 
    
    
    
    
    
    