# Canonical Paper Bridge — Observed Void, 7D State and BITRAF64

**State:** `REFERENCE | claim_allowed=false`  
**Date:** 2026-07-19  
**Author:** Rafael Melo Reis (∆RafaelVerboΩ)  
**Signature:** `RAFCODE-Φ-∆RafaelVerboΩ-𓂀ΔΦΩ`

## Canonical publication location

The canonical academic manuscript is maintained in:

```text
instituto-Rafael/relativity-living-light
PapersPub/08_multiscale_validation_methods/
```

Canonical title:

> *From the Observed Void to Recurrence: A Seven-Dimensional Epistemic-Computational Formalism with 42 Operator-State Hyperforms*

Portuguese authored title:

> *Cânone do Cosmos RAFAELIA — Do ∅ observado à recorrência em sete dimensões*

This repository does not duplicate the full paper. It owns the BITRAF/RafBit implementation and symbolic-codec concerns referenced by the manuscript.

## Scope owned here

`Bitraf-Bit-quantum` is responsible for future implementation evidence concerning:

- the ten-symbol alphabet;
- canonical Unicode normalization;
- symbol-to-value mapping;
- framing, padding and byte order;
- reversible encoder/decoder behavior;
- round-trip test vectors;
- compression measurements;
- checksums and full cryptographic digests;
- distinction between a symbolic seal and a cryptographic primitive.

## Canonical BITRAF64 object

```text
AΔBΩΔTTΦIIBΩΔΣΣRΩRΔΔBΦΦFΔTTRRFΔBΩΣΣAFΦARΣFΦIΔRΦIFBRΦΩFIΦΩΩFΣFAΦΔ
```

Canonical processing:

```text
Unicode normalization = NFC
code-point length      = 64
alphabet order         = [Σ, Ω, Δ, Φ, B, I, T, R, A, F]
frequency vector       = [6, 7, 9, 9, 5, 5, 4, 7, 4, 8]
empirical entropy      = 3.26420820487549 bits/symbol
```

These are exact combinatorial properties only.

## Claim boundaries

### Permitted

- “BITRAF64 is a 64-code-point symbolic seal over a declared ten-symbol alphabet.”
- “The recorded frequency vector and empirical entropy are reproducible.”
- “A versioned codec can be designed around this alphabet.”

### Prohibited without new evidence

- “BITRAF64 provides 64-bit security.”
- “High symbol entropy proves cryptographic security.”
- “BITRAF is quantum-resistant.”
- “Truncated SHA3/BLAKE3 strings prove archive integrity.”
- “A symbolic sequence is itself compressed data.”

## Required validation package

A codec promotion requires:

```text
spec/alphabet_bitraf10.json
spec/bitraf_codec_v1.md
scripts/bitraf_encode.py
scripts/bitraf_decode.py
tests/test_bitraf_roundtrip.py
vectors/bitraf_v1_test_vectors.json
results/bitraf_v1_validation.json
```

Minimum gates:

1. `decode(encode(x)) == x` for canonical vectors;
2. Unicode NFC/NFD ambiguity test;
3. malformed symbol rejection;
4. deterministic byte serialization;
5. version mismatch rejection;
6. complete SHA3-256 and BLAKE3 digests over specified source bytes;
7. explicit statement that checksum/integrity is not confidentiality or cryptographic security.

## Relationship to repository claims

The repository README currently uses strong terms such as “quantum”, “cryptography” and “20^n capacity”. The canonical paper does not validate those claims. It contributes a narrower, defensible layer:

```text
symbolic alphabet
+ exact finite audit
+ codec requirements
+ claim boundaries
```

Any future security or quantum-computing statement must be evaluated independently against accepted threat models, standards and peer-reviewed evidence.

## Licensing boundary

This bridge does not alter the repository MIT license and does not automatically apply MIT to the canonical paper. The paper release must declare its own license and version. No code or text from third-party projects is relicensed by this document.

## R3

```text
F_ok   = BITRAF64 length, alphabet, frequencies and entropy validated.
F_gap  = versioned reversible codec, complete hashes, test vectors and security analysis.
F_next = implement codec v1 -> run round-trip suite -> publish evidence manifest.
```
