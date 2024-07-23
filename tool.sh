#!/bin/bash

echo -e """\033[1;31m 

   ____      _       __   _____           _ 
  / ___|_ __(_) ___ / _| |_   _|__   ___ | |
 | |  _| '__| |/ _ \ |_    | |/ _ \ / _ \| |
 | |_| | |  | |  __/  _|   | | (_) | (_) | |
  \____|_|  |_|\___|_|     |_|\___/ \___/|_|
    Made By (xllor) (hash)                                          
"""
echo "{1} McpTool"
echo "{2} Griefing Tool"
echo "{3} Port Scaner"
echo "{4} Griefing-commands"
echo "{5} H4MTool"
read -p "Lütfen bir seçenek seçin: " option

case $option in
    1)
        pip install mcptool
        mcptool
        ;;       
    2)
        python3 Griefing_tool.py
        ;;
        
    3)
        python3 rustscan.py
        ;;
    4)    
        cat Griefing_Commands.txt
        ;;
        
    5)    
        cd H4MTool
        python h4mtool.py
        ;;
      
            
   *) echo "Geçersiz seçim!" ;;
esac
