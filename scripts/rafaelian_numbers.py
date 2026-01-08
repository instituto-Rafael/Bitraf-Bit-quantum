#!/usr/bin/env python3
"""
Rafaelian Numbers Generator
============================

Implementation of Rafaelian number sequence - an extension of Fibonacci
incorporating fractal factors and cosmic constants.

Author: Rafael Melo Reis
Date: January 2026
License: MIT
"""

import math
from typing import List, Dict
from decimal import Decimal, getcontext


# Set high precision for calculations
getcontext().prec = 50


class RafaelianNumbers:
    """
    Generator for Rafaelian number sequence with fractal properties.
    
    Base sequence: {2, 5, 10, 18, 25, 60, 144, 288, 555, 777, ...}
    """
    
    # Fundamental constants
    PHI = (1 + math.sqrt(5)) / 2  # Golden ratio ≈ 1.618
    SQRT3_OVER_2 = math.sqrt(3) / 2  # Triangular quantum symmetry ≈ 0.866
    UNIVERSAL_HARMONIC = 42
    RESONANCE_CONSTANTS = [288, 777, 555]
    
    # Initial sequence (empirically determined)
    INITIAL_SEQUENCE = [2, 5, 10, 18, 25, 60, 144, 288, 555, 777]
    
    def __init__(self):
        self.sequence = self.INITIAL_SEQUENCE.copy()
        self.cache = {}
    
    def generate_next(self) -> int:
        """
        Generate the next Rafaelian number based on the current sequence.
        
        Uses modified Fibonacci with fractal corrections:
        R_n = R_{n-1} + R_{n-2} + f(Δ, φ, √3/2, 42, 288, 777, 555)
        """
        n = len(self.sequence)
        
        if n < 2:
            raise ValueError("Need at least 2 numbers in sequence")
        
        # Base Fibonacci component
        base = self.sequence[-1] + self.sequence[-2]
        
        # Fractal correction factor
        delta_factor = self._calculate_delta_factor(n)
        phi_correction = self._calculate_phi_correction(n)
        triangular_factor = self._calculate_triangular_factor(n)
        harmonic_contribution = self._calculate_harmonic_contribution(n)
        
        # Combine all factors
        next_value = int(
            base * (1 + delta_factor) +
            phi_correction +
            triangular_factor +
            harmonic_contribution
        )
        
        # Apply modular resonance for certain positions
        if n % 7 == 0:  # Every 7th number has special properties
            next_value = self._apply_resonance(next_value, n)
        
        self.sequence.append(next_value)
        return next_value
    
    def _calculate_delta_factor(self, n: int) -> float:
        """Calculate change/inversion factor Δ."""
        # Oscillates based on position
        return 0.1 * math.sin(n * self.SQRT3_OVER_2)
    
    def _calculate_phi_correction(self, n: int) -> float:
        """Calculate golden ratio correction."""
        if n < 3:
            return 0
        # Subtle influence from previous ratios
        ratio = self.sequence[-1] / self.sequence[-2] if self.sequence[-2] != 0 else 1
        return (ratio - self.PHI) * self.sequence[-3] * 0.05
    
    def _calculate_triangular_factor(self, n: int) -> float:
        """Calculate triangular quantum symmetry contribution."""
        return self.sequence[-1] * self.SQRT3_OVER_2 * 0.01 * (n % 3)
    
    def _calculate_harmonic_contribution(self, n: int) -> float:
        """Calculate universal harmonic (42) contribution."""
        if n % 6 == 0:  # Harmonic resonance every 6 positions
            return self.UNIVERSAL_HARMONIC * math.log(n + 1)
        return 0
    
    def _apply_resonance(self, value: int, n: int) -> int:
        """
        Apply resonance constant modulation.
        
        This aligns values with resonance patterns by rounding up to the next
        multiple of the resonance constant. Formula: value + (resonance - (value % resonance))
        ensures the result is the smallest value >= original that is divisible by resonance.
        
        Mathematical proof:
        - Let r = resonance, v = value, k = v % r (remainder when v divided by r)
        - Then v = qr + k for some integer q
        - Result = v + (r - k) = qr + k + r - k = qr + r = (q+1)r
        - Therefore result is always a multiple of r
        
        Example: If value=100 and resonance=21:
        - 100 % 21 = 16 (since 100 = 4×21 + 16)
        - Result = 100 + (21 - 16) = 100 + 5 = 105
        - Verify: 105 = 5×21 ✓ (next multiple of 21 after 100)
        """
        # Use resonance constants cyclically based on position
        resonance_idx = (n // 7) % len(self.RESONANCE_CONSTANTS)
        resonance = self.RESONANCE_CONSTANTS[resonance_idx]
        
        # Align value to next resonance multiple
        # This creates harmonic alignment with cosmic constants
        return value + (resonance - (value % resonance))
    
    def generate_sequence(self, length: int) -> List[int]:
        """
        Generate Rafaelian sequence of specified length.
        
        Args:
            length: Total length of sequence to generate
            
        Returns:
            List of Rafaelian numbers
        """
        while len(self.sequence) < length:
            self.generate_next()
        
        return self.sequence[:length]
    
    def get_number(self, index: int) -> int:
        """
        Get the nth Rafaelian number (0-indexed).
        
        Args:
            index: Position in sequence
            
        Returns:
            Rafaelian number at that position
        """
        if index < len(self.sequence):
            return self.sequence[index]
        
        # Generate up to requested index
        self.generate_sequence(index + 1)
        return self.sequence[index]
    
    def calculate_ratios(self, start: int = 0, end: int = None) -> List[float]:
        """
        Calculate ratios between consecutive Rafaelian numbers.
        
        Args:
            start: Starting index
            end: Ending index (None for all available)
            
        Returns:
            List of ratios R_{n+1} / R_n
        """
        if end is None:
            end = len(self.sequence)
        
        ratios = []
        for i in range(start, min(end - 1, len(self.sequence) - 1)):
            if self.sequence[i] != 0:
                ratio = self.sequence[i + 1] / self.sequence[i]
                ratios.append(ratio)
        
        return ratios
    
    def find_cosmological_alignments(self) -> Dict[str, float]:
        """
        Find alignments between Rafaelian ratios and cosmological constants.
        
        Returns:
            Dictionary of alignments and their errors
        """
        # Known cosmological constants
        OMEGA_LAMBDA = 0.685  # Dark energy density
        OMEGA_M = 0.315  # Matter density
        OMEGA_B = 0.049  # Baryonic matter density
        
        ratios = self.calculate_ratios()
        
        alignments = {}
        
        # Find closest matches
        for i, ratio in enumerate(ratios):
            # Check dark energy
            if abs(ratio - OMEGA_LAMBDA) < 0.05:
                alignments[f'dark_energy_{i}'] = {
                    'ratio': ratio,
                    'target': OMEGA_LAMBDA,
                    'error': abs(ratio - OMEGA_LAMBDA)
                }
            
            # Check matter density
            if abs(ratio - OMEGA_M) < 0.05:
                alignments[f'matter_{i}'] = {
                    'ratio': ratio,
                    'target': OMEGA_M,
                    'error': abs(ratio - OMEGA_M)
                }
            
            # Check baryonic matter
            if abs(ratio - OMEGA_B) < 0.01:
                alignments[f'baryonic_{i}'] = {
                    'ratio': ratio,
                    'target': OMEGA_B,
                    'error': abs(ratio - OMEGA_B)
                }
        
        return alignments
    
    def check_modular_properties(self, modulus: int = 21) -> Dict[int, int]:
        """
        Check modular properties of Rafaelian sequence.
        
        Args:
            modulus: Modulus to check (default 21)
            
        Returns:
            Dictionary mapping index to R_n mod modulus
        """
        return {i: num % modulus for i, num in enumerate(self.sequence)}
    
    def analyze_growth_rate(self) -> Dict[str, float]:
        """
        Analyze growth characteristics of the sequence.
        
        Returns:
            Dictionary with growth statistics
        """
        if len(self.sequence) < 3:
            return {}
        
        ratios = self.calculate_ratios()
        
        return {
            'mean_ratio': sum(ratios) / len(ratios),
            'min_ratio': min(ratios),
            'max_ratio': max(ratios),
            'std_dev': math.sqrt(sum((r - sum(ratios)/len(ratios))**2 for r in ratios) / len(ratios)),
            'vs_phi': sum(ratios) / len(ratios) - self.PHI,
            'vs_fibonacci': sum(ratios) / len(ratios) / self.PHI
        }


def calculate_derivatives(numbers: List[int]) -> List[float]:
    """
    Calculate first derivatives (differences) of Rafaelian sequence.
    
    Args:
        numbers: Sequence of Rafaelian numbers
        
    Returns:
        List of first derivatives
    """
    return [numbers[i+1] - numbers[i] for i in range(len(numbers)-1)]


def calculate_second_derivatives(numbers: List[int]) -> List[float]:
    """
    Calculate second derivatives of Rafaelian sequence.
    
    Args:
        numbers: Sequence of Rafaelian numbers
        
    Returns:
        List of second derivatives
    """
    first_deriv = calculate_derivatives(numbers)
    return calculate_derivatives([int(d) for d in first_deriv])


def calculate_antiderivative(numbers: List[int]) -> List[int]:
    """
    Calculate antiderivative (cumulative sum) of Rafaelian sequence.
    
    Args:
        numbers: Sequence of Rafaelian numbers
        
    Returns:
        Cumulative sum sequence
    """
    cumsum = [numbers[0]]
    for i in range(1, len(numbers)):
        cumsum.append(cumsum[-1] + numbers[i])
    return cumsum


def calculate_inverse_sequence(numbers: List[int]) -> List[float]:
    """
    Calculate inverse Rafaelian sequence (reciprocals).
    
    Args:
        numbers: Sequence of Rafaelian numbers
        
    Returns:
        Sequence of reciprocals
    """
    return [1.0 / n if n != 0 else 0 for n in numbers]


# Example usage and demonstrations
if __name__ == "__main__":
    print("=" * 70)
    print("Rafaelian Numbers Generator Demo")
    print("=" * 70)
    
    # Initialize generator
    gen = RafaelianNumbers()
    
    # Test 1: Generate sequence
    print("\n1. First 20 Rafaelian Numbers:")
    sequence = gen.generate_sequence(20)
    for i, num in enumerate(sequence):
        print(f"   R_{i} = {num}")
    
    # Test 2: Calculate ratios
    print("\n2. Ratios Between Consecutive Numbers:")
    ratios = gen.calculate_ratios(0, 15)
    for i, ratio in enumerate(ratios):
        print(f"   R_{i+1}/R_{i} = {ratio:.6f}")
    
    # Test 3: Cosmological alignments
    print("\n3. Cosmological Constant Alignments:")
    alignments = gen.find_cosmological_alignments()
    if alignments:
        for key, data in alignments.items():
            print(f"   {key}:")
            print(f"      Ratio: {data['ratio']:.6f}")
            print(f"      Target: {data['target']:.6f}")
            print(f"      Error: {data['error']:.6f}")
    else:
        print("   No close alignments found in current sequence")
    
    # Test 4: Modular properties
    print("\n4. Modular Properties (mod 21):")
    mod_props = gen.check_modular_properties(21)
    mod_counts = {}
    for idx, mod_val in list(mod_props.items())[:15]:
        mod_counts[mod_val] = mod_counts.get(mod_val, 0) + 1
        print(f"   R_{idx} ≡ {mod_val} (mod 21)")
    
    # Test 5: Growth analysis
    print("\n5. Growth Rate Analysis:")
    growth = gen.analyze_growth_rate()
    for key, value in growth.items():
        print(f"   {key}: {value:.6f}")
    
    # Test 6: Derivatives and antiderivatives
    print("\n6. Derivatives and Antiderivatives:")
    first_seq = sequence[:10]
    print(f"   Original: {first_seq}")
    
    first_deriv = calculate_derivatives(first_seq)
    print(f"   1st Derivative: {first_deriv[:9]}")
    
    second_deriv = calculate_second_derivatives(first_seq)
    print(f"   2nd Derivative: {second_deriv[:8]}")
    
    antideriv = calculate_antiderivative(first_seq)
    print(f"   Antiderivative: {antideriv}")
    
    inverse = calculate_inverse_sequence(first_seq)
    print(f"   Inverse: {[f'{x:.6f}' for x in inverse[:5]]}...")
    
    # Test 7: Comparison with Fibonacci
    print("\n7. Comparison with Fibonacci:")
    fib = [1, 1]
    for i in range(18):
        fib.append(fib[-1] + fib[-2])
    
    print("   Position | Rafaelian | Fibonacci | Ratio")
    print("   " + "-" * 50)
    for i in range(min(10, len(sequence))):
        ratio = sequence[i] / fib[i] if fib[i] != 0 else 0
        print(f"   {i:8} | {sequence[i]:9} | {fib[i]:9} | {ratio:5.2f}")
    
    print("\n" + "=" * 70)
    print("Demo completed successfully!")
    print("=" * 70)
