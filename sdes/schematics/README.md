components used to implement SDES

# Component list

| Component | Purpose |
| --- | --- |
| [16to2](16to2%20rom.litematic) | |
| [5shift1left](5shift1left.litematic) | |
| [the clock](clock%20that%20kills%20itself.litematic) | |
| [ep](ep.litematic) | |
| [fiestal_v1](fiestal_v1.litematic) | |
| [IP'](IP%27.litematic) | |
| [IP](IP.litematic) | |
| [keygen](keygen.litematic) | |
| [nibble_shift v1](nibble_shift_v1.litematic) | |
| [p10](p10.litematic) | |
| [p4](p4.litematic) | |
| [sbox0](sbox0.litematic) | |
| [sbox1](sbox1.litematic) | |
| [ui_v1](ui_v1.litematic) | |

# Buggy components

Some of these components are buggy and had to be patched in the fully assembled circuit

16to2 rom has a broken decoder and also allows signals from output bit 1 to leak into bit 0
- this impacts sbox0 and sbox1 which are built on the rom

nibbleshift, p8, and p4 use pistons to transmit signals downwards which tend to be unreliable, they can be replaced with spiral staircases
fiestal rounds are broken as a result of bugged components
