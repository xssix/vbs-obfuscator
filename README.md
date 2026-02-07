<p align="center">
  <img src="https://img.shields.io/badge/Security-Advanced-red?style=for-the-badge&logo=probot" />
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows" />
</p>

# VBS-OBF

Minimalist, high-intensity VBScript protection.

### Capabilities
- **Polymorphic Logic**: Multi-iteration dynamic key derivation.
- **Dual Layer**: Nested execution stubs with independent XOR keys.
- **Visual Noise**: Entropy-based variable naming.
- **Payload Stealth**: Byte-stream encapsulation using `x` separation.

### Usage
```bash
python obfuscator.py in.vbs -o out.vbs
```


| Spec | Value |
| :--- | :--- |
| **Type** | VBS |
| **Logic** | Recursive XOR |
| **Iterations** | 60+ |
| **Working** | as of 2026 |
