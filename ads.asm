.global _start

_start:
  MOV R1, #0xA
  ADD R0, R1, #0x14
  SWI 0
  MOV R7, #1
  SWI 0