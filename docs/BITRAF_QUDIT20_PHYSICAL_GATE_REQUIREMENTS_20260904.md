# BITRAF — 20-State Formalism, Qudit Boundary and Physical Gate Requirements

**Date:** 2026-09-04  
**Status:** `REVIEWED_FAIL_CLOSED`  
**claim_allowed:** `false`

## 1. Purpose

This record preserves the authorial BITRAF construction while separating three distinct objects:

1. a classical multistate alphabet;
2. a mathematical 20-dimensional quantum state space;
3. a physical quantum device.

These objects must not be treated as equivalent without evidence.

## 2. Classical state-counting layer

If one BITRAF symbol has 10 labels and an independent binary parity, then the classical alphabet has:

\[
|\mathcal A|=10\times2=20.
\]

For `n` independent classical symbols:

\[
|\mathcal A^n|=20^n.
\]

The maximum classical information carried by one uniformly distributed 20-state symbol is:

\[
\log_2 20\approx4.321928\ \text{bits}.
\]

Therefore state-counting alone does not imply an algorithmic speedup of `10^n` over binary computation.

## 3. Qudit-compatible mathematical layer

A quantum 20-level system can be modeled by:

\[
\mathcal H_{20}=\mathbb C^{20}
\]

with normalized state:

\[
|\psi\rangle=\sum_{j=0}^{19}\alpha_j|j\rangle,
\qquad
\sum_{j=0}^{19}|\alpha_j|^2=1.
\]

This is mathematically compatible with the established qudit formalism. The scientific novelty of BITRAF therefore cannot be claimed solely from the dimension `20`; it must come from a distinct and demonstrated structure such as:

- gate algebra;
- native error correction;
- encoding/decoding;
- fault-tolerance construction;
- hardware realization;
- benchmark advantage under controlled comparison.

## 4. Required physical object

A physical BITRAF quantum unit requires at minimum:

\[
\mathcal Q_{20}=(\mathcal H_{20},\mathcal G,\mathcal M,\mathcal N,\mathcal C)
\]

where:

- \(\mathcal H_{20}\): physical 20-level computational subspace;
- \(\mathcal G\): calibrated gate set;
- \(\mathcal M\): measurement/readout model;
- \(\mathcal N\): experimentally characterized noise channel;
- \(\mathcal C\): control system mapping commands to physical operations.

## 5. Minimum evidence gates

### GATE-BQ-01 — state preparation

Demonstrate repeatable preparation of basis states and selected superpositions.

Required evidence:

- preparation fidelity;
- calibration procedure;
- confusion matrix;
- raw experimental records.

### GATE-BQ-02 — coherent control

Demonstrate at least a universal or explicitly bounded gate family over the declared computational subspace.

Required evidence:

- target unitary;
- pulse/control description;
- gate fidelity;
- reproducible calibration.

### GATE-BQ-03 — coherence/noise

Measure, where physically applicable:

\[
T_1,\quad T_2,\quad F_{prep},\quad F_{gate},\quad F_{readout}.
\]

For platforms where `T1/T2` are not the natural descriptors, record the platform-appropriate coherence and noise observables instead of forcing these labels.

### GATE-BQ-04 — multipartite operation

Demonstrate at least one nontrivial interaction between two physical BITRAF units or a justified logical equivalent.

Correlation alone is insufficient; the protocol must specify what quantum resource is claimed and how it is tested.

### GATE-BQ-05 — computational benchmark

Compare against a declared baseline with equal problem definition, precision target, resource accounting and error budget.

State-space cardinality is not itself a runtime benchmark.

### GATE-BQ-06 — error correction

Any Tag14 or BITRAF-native correction claim must specify:

- code space;
- error model;
- parity/check operators;
- decoder;
- threshold or measured error-rate reduction;
- independent test vectors.

Claims such as `99.7% correction` remain `TOKEN_VAZIO` until the underlying corpus/run receipts are present.

## 6. Cryptographic boundary

A 20-state alphabet does not imply post-quantum security.

Any claim that Shor, Grover or other quantum attacks are inapplicable must be justified against a precisely specified cryptosystem and security reduction.

Required status until then:

`BITRAF_POST_QUANTUM_SECURITY=TOKEN_VAZIO`.

## 7. Cosmology and biology boundary

Mappings from BITRAF symbols to cosmological density fractions, DNA, mutation classes or other physical/biological systems are authorial models until they include:

- units and dimensional consistency;
- data provenance;
- train/test or fit/validation separation;
- null model;
- uncertainty;
- falsifier;
- independent reproduction.

## 8. Internal consistency correction

Two different state-counting conventions must not be mixed:

- 10 states: \(10^n/2^n=5^n\);
- 20 states: \(20^n/2^n=10^n\).

For `n=10`, `9,765,625` corresponds to \(5^{10}\), therefore to the 10-state-vs-binary ratio, not to the 20-state-vs-binary ratio.

## 9. Current epistemic state

```yaml
BITRAF_CLASSICAL_20_STATE_ALPHABET: VALID_DEFINITION
BITRAF_HILBERT20_MODEL: MATHEMATICALLY_VALID
BITRAF_DISTINCT_QUANTUM_GATE_ALGEBRA: TOKEN_VAZIO
BITRAF_PHYSICAL_CHIP: TOKEN_VAZIO
BITRAF_MULTIPARTITE_QUANTUM_OPERATION: TOKEN_VAZIO
TAG14_MEASURED_ERROR_CORRECTION: TOKEN_VAZIO
POST_QUANTUM_SECURITY: TOKEN_VAZIO
COSMOLOGICAL_VALIDATION: TOKEN_VAZIO
BIOLOGICAL_VALIDATION: TOKEN_VAZIO
claim_allowed: false
```

## 10. Next verifiable action

Build a finite `BITRAF-Q20` simulator with:

- explicit basis ordering;
- unitary gate definitions;
- measurement model;
- noise channel;
- deterministic test vectors;
- comparison with standard qudit constructions.

Only after the mathematical gate model is closed should a physical-device claim be promoted.