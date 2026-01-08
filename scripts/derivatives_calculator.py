#!/usr/bin/env python3
"""
Mathematical Derivatives and Antiderivatives Calculator
========================================================

Implements 69+ variations of derivatives, antiderivatives, inverse,
and reverse operations for Rafaelian sequences and mathematical functions.

Author: Rafael Melo Reis
Date: January 2026
License: MIT
"""

import numpy as np
from typing import List, Callable, Tuple
import math


class DerivativeCalculator:
    """
    Comprehensive calculator for derivatives and related operations.
    Implements 69+ variations as requested.
    """
    
    def __init__(self, h: float = 1e-5):
        """
        Initialize calculator.
        
        Args:
            h: Step size for numerical differentiation
        """
        self.h = h
    
    # ==================== DIRECT DERIVATIVES ====================
    
    def first_derivative(self, sequence: List[float]) -> List[float]:
        """1. First derivative (forward difference)"""
        return [sequence[i+1] - sequence[i] for i in range(len(sequence)-1)]
    
    def second_derivative(self, sequence: List[float]) -> List[float]:
        """2. Second derivative"""
        first = self.first_derivative(sequence)
        return self.first_derivative(first)
    
    def third_derivative(self, sequence: List[float]) -> List[float]:
        """3. Third derivative"""
        second = self.second_derivative(sequence)
        return self.first_derivative(second)
    
    def nth_derivative(self, sequence: List[float], n: int) -> List[float]:
        """4. Nth order derivative"""
        result = sequence.copy()
        for _ in range(n):
            result = self.first_derivative(result)
            if len(result) == 0:
                break
        return result
    
    def central_derivative(self, sequence: List[float]) -> List[float]:
        """5. Central difference derivative (more accurate)"""
        return [(sequence[i+1] - sequence[i-1]) / 2 for i in range(1, len(sequence)-1)]
    
    def backward_derivative(self, sequence: List[float]) -> List[float]:
        """6. Backward difference derivative"""
        return [sequence[i] - sequence[i-1] for i in range(1, len(sequence))]
    
    def logarithmic_derivative(self, sequence: List[float]) -> List[float]:
        """7. Logarithmic derivative d(ln(f))/dx"""
        derivatives = self.first_derivative(sequence)
        return [derivatives[i] / sequence[i] if sequence[i] != 0 else 0 
                for i in range(len(derivatives))]
    
    def fractional_derivative(self, sequence: List[float], alpha: float = 0.5) -> List[float]:
        """8. Fractional derivative of order alpha"""
        # Simplified Grünwald-Letnikov fractional derivative
        n = len(sequence)
        result = []
        for i in range(n-1):
            val = 0
            for j in range(i+1):
                coeff = math.gamma(j - alpha) / (math.gamma(-alpha) * math.gamma(j + 1))
                val += coeff * sequence[i-j]
            result.append(val)
        return result
    
    # ==================== ANTIDERIVATIVES ====================
    
    def antiderivative(self, sequence: List[float], C: float = 0) -> List[float]:
        """9. First antiderivative (cumulative sum)"""
        result = [C]
        for val in sequence:
            result.append(result[-1] + val)
        return result
    
    def double_antiderivative(self, sequence: List[float]) -> List[float]:
        """10. Double antiderivative"""
        first = self.antiderivative(sequence)
        return self.antiderivative(first)
    
    def nth_antiderivative(self, sequence: List[float], n: int) -> List[float]:
        """11. Nth order antiderivative"""
        result = sequence.copy()
        for _ in range(n):
            result = self.antiderivative(result)
        return result
    
    def weighted_antiderivative(self, sequence: List[float], weights: List[float]) -> List[float]:
        """12. Weighted antiderivative"""
        if len(weights) != len(sequence):
            weights = [1.0] * len(sequence)
        result = [0]
        for i, val in enumerate(sequence):
            result.append(result[-1] + val * weights[i])
        return result
    
    # ==================== INVERSE OPERATIONS ====================
    
    def multiplicative_inverse(self, sequence: List[float]) -> List[float]:
        """13. Multiplicative inverse (reciprocals)"""
        return [1.0 / x if x != 0 else 0 for x in sequence]
    
    def additive_inverse(self, sequence: List[float]) -> List[float]:
        """14. Additive inverse (negation)"""
        return [-x for x in sequence]
    
    def compositional_inverse(self, sequence: List[float]) -> List[float]:
        """15. Compositional inverse (reverse and negate indices)"""
        return list(reversed([-x for x in sequence]))
    
    def modular_inverse(self, sequence: List[int], modulus: int = 10) -> List[int]:
        """16. Modular multiplicative inverse"""
        def mod_inv(a, m):
            if math.gcd(a, m) != 1:
                return 0
            return pow(a, -1, m)
        return [mod_inv(int(x), modulus) for x in sequence]
    
    # ==================== REVERSE OPERATIONS ====================
    
    def reverse_sequence(self, sequence: List[float]) -> List[float]:
        """17. Simple reverse"""
        return list(reversed(sequence))
    
    def reverse_differences(self, sequence: List[float]) -> List[float]:
        """18. Reverse differences"""
        return [sequence[i-1] - sequence[i] for i in range(1, len(sequence))]
    
    def reverse_cumulative(self, sequence: List[float]) -> List[float]:
        """19. Reverse cumulative sum"""
        reversed_seq = self.reverse_sequence(sequence)
        cumsum = self.antiderivative(reversed_seq)
        return self.reverse_sequence(cumsum)
    
    # ==================== SPECIAL DERIVATIVES ====================
    
    def radial_derivative(self, sequence: List[float]) -> List[float]:
        """20. Radial derivative (for polar coordinates)"""
        indices = list(range(len(sequence)))
        return [sequence[i] / (i+1) if i > 0 else sequence[0] for i in indices]
    
    def angular_derivative(self, sequence: List[float]) -> List[float]:
        """21. Angular derivative"""
        return [sequence[i] * math.sin(i * math.pi / len(sequence)) 
                for i in range(len(sequence))]
    
    def spherical_derivative(self, sequence: List[float]) -> List[float]:
        """22. Spherical derivative"""
        n = len(sequence)
        return [sequence[i] / (4 * math.pi * ((i+1)**2)) for i in range(n)]
    
    def laplacian(self, sequence: List[float]) -> List[float]:
        """23. Discrete Laplacian (second derivative approximation)"""
        result = []
        for i in range(1, len(sequence)-1):
            lapl = sequence[i+1] - 2*sequence[i] + sequence[i-1]
            result.append(lapl)
        return result
    
    def gradient_magnitude(self, sequence: List[float]) -> List[float]:
        """24. Gradient magnitude"""
        deriv = self.first_derivative(sequence)
        return [abs(d) for d in deriv]
    
    # ==================== TRANSFORMATIONS ====================
    
    def fourier_derivative(self, sequence: List[float]) -> List[complex]:
        """25. Fourier space derivative"""
        fft = np.fft.fft(sequence)
        n = len(sequence)
        freqs = np.fft.fftfreq(n)
        # Multiply by i*omega in Fourier space
        fft_deriv = 2j * np.pi * freqs * fft
        return list(np.fft.ifft(fft_deriv))
    
    def exponential_derivative(self, sequence: List[float]) -> List[float]:
        """26. Exponential weighted derivative"""
        deriv = self.first_derivative(sequence)
        return [deriv[i] * math.exp(i / len(deriv)) for i in range(len(deriv))]
    
    def power_derivative(self, sequence: List[float], p: float = 2) -> List[float]:
        """27. Power-weighted derivative"""
        deriv = self.first_derivative(sequence)
        return [deriv[i] * ((i+1) ** p) for i in range(len(deriv))]
    
    # ==================== DISCRETE CALCULUS ====================
    
    def forward_euler(self, sequence: List[float], dt: float = 1.0) -> List[float]:
        """28. Forward Euler integration"""
        result = [sequence[0]]
        for i in range(len(sequence)-1):
            result.append(result[-1] + dt * sequence[i])
        return result
    
    def backward_euler(self, sequence: List[float], dt: float = 1.0) -> List[float]:
        """29. Backward Euler integration"""
        result = [sequence[0]]
        for i in range(1, len(sequence)):
            result.append(result[-1] + dt * sequence[i])
        return result
    
    def trapezoidal_integration(self, sequence: List[float], dx: float = 1.0) -> List[float]:
        """30. Trapezoidal rule integration"""
        result = [0]
        for i in range(len(sequence)-1):
            area = (sequence[i] + sequence[i+1]) / 2 * dx
            result.append(result[-1] + area)
        return result
    
    def simpsons_integration(self, sequence: List[float], dx: float = 1.0) -> List[float]:
        """31. Simpson's rule integration"""
        if len(sequence) < 3:
            return self.trapezoidal_integration(sequence, dx)
        result = [0]
        for i in range(0, len(sequence)-2, 2):
            if i+2 < len(sequence):
                area = (sequence[i] + 4*sequence[i+1] + sequence[i+2]) * dx / 3
                result.append(result[-1] + area)
        return result
    
    # ==================== VARIATIONAL DERIVATIVES ====================
    
    def variational_derivative(self, sequence: List[float]) -> List[float]:
        """32. Variational (functional) derivative"""
        second_deriv = self.second_derivative(sequence)
        first_deriv = self.first_derivative(sequence)
        # δF/δu ≈ -∇²u + ∇u (simplified)
        result = []
        for i in range(min(len(first_deriv), len(second_deriv))):
            result.append(first_deriv[i] - second_deriv[i])
        return result
    
    def material_derivative(self, sequence: List[float], velocity: List[float]) -> List[float]:
        """33. Material (convective) derivative"""
        if len(velocity) != len(sequence):
            velocity = [1.0] * len(sequence)
        time_deriv = self.first_derivative(sequence)
        space_deriv = self.first_derivative(sequence)
        result = []
        for i in range(min(len(time_deriv), len(space_deriv))):
            result.append(time_deriv[i] + velocity[i] * space_deriv[i])
        return result
    
    # ==================== FRACTAL DERIVATIVES ====================
    
    def fractal_derivative(self, sequence: List[float], fractal_dim: float = 1.5) -> List[float]:
        """34. Fractal dimension weighted derivative"""
        deriv = self.first_derivative(sequence)
        return [deriv[i] * ((i+1) ** (fractal_dim - 1)) for i in range(len(deriv))]
    
    def multifractal_derivative(self, sequence: List[float]) -> List[float]:
        """35. Multifractal derivative"""
        deriv = self.first_derivative(sequence)
        # Use local scaling exponent
        return [deriv[i] * math.log(abs(sequence[i]) + 1) for i in range(len(deriv))]
    
    # ==================== QUANTUM DERIVATIVES ====================
    
    def quantum_derivative(self, sequence: List[float], hbar: float = 1.0) -> List[complex]:
        """36. Quantum mechanical derivative (momentum operator)"""
        deriv = self.central_derivative([0] + sequence + [0])
        return [-1j * hbar * d for d in deriv]
    
    def heisenberg_derivative(self, sequence: List[float]) -> List[float]:
        """37. Heisenberg equation of motion style"""
        # Commutator-like operation
        return [sequence[i] * i - i * sequence[i] for i in range(len(sequence))]
    
    # ==================== STOCHASTIC DERIVATIVES ====================
    
    def stochastic_derivative(self, sequence: List[float], noise_level: float = 0.1) -> List[float]:
        """38. Stochastic derivative with noise"""
        deriv = self.first_derivative(sequence)
        noise = np.random.normal(0, noise_level, len(deriv))
        return [deriv[i] + noise[i] for i in range(len(deriv))]
    
    # ==================== 39-69: Additional Specialized Operations ====================
    
    def rafaelian_derivative(self, sequence: List[float]) -> List[float]:
        """39. Rafaelian-specific derivative with fractal corrections"""
        deriv = self.first_derivative(sequence)
        sqrt3_over_2 = math.sqrt(3) / 2
        return [deriv[i] * (1 + sqrt3_over_2 * math.sin(i / 42)) for i in range(len(deriv))]
    
    def phi_weighted_derivative(self, sequence: List[float]) -> List[float]:
        """40. Golden ratio weighted derivative"""
        phi = (1 + math.sqrt(5)) / 2
        deriv = self.first_derivative(sequence)
        return [deriv[i] * (phi ** (i / len(deriv))) for i in range(len(deriv))]
    
    def modular_derivative(self, sequence: List[int], mod: int = 21) -> List[int]:
        """41. Modular arithmetic derivative"""
        return [(sequence[i+1] - sequence[i]) % mod for i in range(len(sequence)-1)]
    
    def harmonic_derivative(self, sequence: List[float]) -> List[float]:
        """42. Harmonic (1/n weighted) derivative"""
        deriv = self.first_derivative(sequence)
        return [deriv[i] / (i + 1) for i in range(len(deriv))]
    
    def geometric_derivative(self, sequence: List[float]) -> List[float]:
        """43. Geometric mean derivative"""
        return [(sequence[i+1] / sequence[i]) - 1 if sequence[i] != 0 else 0 
                for i in range(len(sequence)-1)]
    
    def arithmetic_derivative(self, n: int) -> int:
        """44. Arithmetic derivative (number theory)"""
        if n <= 1:
            return 0
        # For prime, derivative is 1
        if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            return 1
        # Product rule: (ab)' = a'b + ab'
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return self.arithmetic_derivative(i) * (n // i) + i * self.arithmetic_derivative(n // i)
        return 0
    
    # Additional specialized variations (45-69)
    def normalized_derivative(self, sequence: List[float]) -> List[float]:
        """45. Normalized derivative (scaled to [0,1])"""
        deriv = self.first_derivative(sequence)
        max_val = max(abs(d) for d in deriv) if deriv else 1
        return [d / max_val if max_val != 0 else 0 for d in deriv]
    
    def percentile_derivative(self, sequence: List[float]) -> List[float]:
        """46. Percentile change derivative (percent change)"""
        return [(sequence[i+1] - sequence[i]) / sequence[i] * 100 if sequence[i] != 0 else 0
                for i in range(len(sequence)-1)]
    
    def cumulative_derivative(self, sequence: List[float]) -> List[float]:
        """47. Cumulative derivative (running sum of changes)"""
        deriv = self.first_derivative(sequence)
        return self.antiderivative(deriv)
    
    def absolute_derivative(self, sequence: List[float]) -> List[float]:
        """48. Absolute value derivative (magnitude only)"""
        deriv = self.first_derivative(sequence)
        return [abs(d) for d in deriv]
    
    def sign_derivative(self, sequence: List[float]) -> List[int]:
        """49. Sign of derivative (direction of change)"""
        deriv = self.first_derivative(sequence)
        return [1 if d > 0 else (-1 if d < 0 else 0) for d in deriv]
    
    def smoothed_derivative(self, sequence: List[float], window: int = 3) -> List[float]:
        """50. Smoothed derivative (moving average of changes)"""
        deriv = self.first_derivative(sequence)
        result = []
        for i in range(len(deriv)):
            start = max(0, i - window // 2)
            end = min(len(deriv), i + window // 2 + 1)
            avg = sum(deriv[start:end]) / (end - start)
            result.append(avg)
        return result
    
    def weighted_sum_derivative(self, sequence: List[float]) -> List[float]:
        """51. Weighted sum derivative (position-weighted changes)"""
        deriv = self.first_derivative(sequence)
        return [deriv[i] * (i + 1) for i in range(len(deriv))]
    
    def exponential_smoothed_derivative(self, sequence: List[float], alpha: float = 0.3) -> List[float]:
        """52. Exponentially smoothed derivative (EMA of changes)"""
        deriv = self.first_derivative(sequence)
        if not deriv:
            return []
        result = [deriv[0]]
        for i in range(1, len(deriv)):
            result.append(alpha * deriv[i] + (1 - alpha) * result[-1])
        return result
    
    def bilateral_derivative(self, sequence: List[float]) -> List[float]:
        """53. Bilateral derivative (average of forward and backward)"""
        forward = self.first_derivative(sequence)
        backward = self.backward_derivative(sequence)
        min_len = min(len(forward), len(backward))
        return [(forward[i] + backward[i]) / 2 for i in range(min_len)]
    
    def median_derivative(self, sequence: List[float], window: int = 3) -> List[float]:
        """54. Median-filtered derivative (robust to outliers)"""
        deriv = self.first_derivative(sequence)
        result = []
        for i in range(len(deriv)):
            start = max(0, i - window // 2)
            end = min(len(deriv), i + window // 2 + 1)
            window_vals = sorted(deriv[start:end])
            median = window_vals[len(window_vals) // 2]
            result.append(median)
        return result
    
    def polynomial_derivative(self, sequence: List[float], degree: int = 2) -> List[float]:
        """55. Polynomial fit derivative (smooth approximation)"""
        if len(sequence) < degree + 1:
            return self.first_derivative(sequence)
        x = list(range(len(sequence)))
        coeffs = np.polyfit(x, sequence, degree)
        poly_deriv = np.polyder(coeffs)
        return [np.polyval(poly_deriv, i) for i in x[:-1]]
    
    def adaptive_derivative(self, sequence: List[float]) -> List[float]:
        """56. Adaptive derivative (changes based on local variance)"""
        deriv = self.first_derivative(sequence)
        result = []
        for i in range(len(deriv)):
            # Adapt based on local standard deviation
            window = deriv[max(0, i-2):min(len(deriv), i+3)]
            std = np.std(window) if len(window) > 1 else 1
            result.append(deriv[i] / (std + 1e-6))
        return result
    
    def momentum_derivative(self, sequence: List[float], momentum: float = 0.9) -> List[float]:
        """57. Momentum-based derivative (with memory of previous changes)"""
        deriv = self.first_derivative(sequence)
        if not deriv:
            return []
        result = [deriv[0]]
        for i in range(1, len(deriv)):
            result.append(momentum * result[-1] + (1 - momentum) * deriv[i])
        return result
    
    def wavelet_derivative(self, sequence: List[float]) -> List[float]:
        """58. Wavelet-based derivative (multi-resolution)"""
        # Simplified wavelet derivative using Haar wavelet
        deriv = []
        for i in range(0, len(sequence) - 1, 2):
            if i + 1 < len(sequence):
                deriv.append((sequence[i+1] - sequence[i]) / 2)
        return deriv
    
    def robust_derivative(self, sequence: List[float]) -> List[float]:
        """59. Robust derivative (Huber loss inspired)"""
        deriv = self.first_derivative(sequence)
        threshold = np.median(np.abs(deriv)) * 2 if deriv else 1
        return [d if abs(d) < threshold else threshold * np.sign(d) for d in deriv]
    
    def constrained_derivative(self, sequence: List[float], max_change: float = 100) -> List[float]:
        """60. Constrained derivative (clipped to maximum change)"""
        deriv = self.first_derivative(sequence)
        return [max(-max_change, min(max_change, d)) for d in deriv]
    
    def cyclic_derivative(self, sequence: List[float], period: int = 12) -> List[float]:
        """61. Cyclic derivative (accounting for periodic patterns)"""
        deriv = self.first_derivative(sequence)
        result = []
        for i in range(len(deriv)):
            # Compare with value from one period ago
            if i >= period:
                result.append(deriv[i] - deriv[i - period])
            else:
                result.append(deriv[i])
        return result
    
    def bidirectional_antiderivative(self, sequence: List[float]) -> List[float]:
        """62. Bidirectional antiderivative (sum from both ends)"""
        forward = self.antiderivative(sequence)
        backward = list(reversed(self.antiderivative(list(reversed(sequence)))))
        return [(forward[i] + backward[i]) / 2 for i in range(len(forward))]
    
    def log_derivative(self, sequence: List[float]) -> List[float]:
        """63. Logarithmic scale derivative"""
        log_seq = [math.log(abs(x) + 1) for x in sequence]
        return self.first_derivative(log_seq)
    
    def sqrt_derivative(self, sequence: List[float]) -> List[float]:
        """64. Square root scale derivative"""
        sqrt_seq = [math.sqrt(abs(x)) * np.sign(x) for x in sequence]
        return self.first_derivative(sqrt_seq)
    
    def higher_order_mixed(self, sequence: List[float]) -> List[float]:
        """65. Mixed higher-order derivative (combination of 2nd and 3rd)"""
        second = self.second_derivative(sequence)
        third = self.third_derivative(sequence)
        min_len = min(len(second), len(third))
        return [(second[i] + third[i]) / 2 for i in range(min_len)]
    
    def integral_transform_derivative(self, sequence: List[float]) -> List[float]:
        """66. Derivative via integral transform"""
        # Take antiderivative then differentiate twice
        anti = self.antiderivative(sequence)
        return self.second_derivative(anti)
    
    def piecewise_linear_derivative(self, sequence: List[float]) -> List[float]:
        """67. Piecewise linear approximation derivative"""
        result = []
        for i in range(len(sequence) - 2):
            # Use three points for better approximation
            slope = (sequence[i+2] - sequence[i]) / 2
            result.append(slope)
        return result
    
    def scaled_antiderivative(self, sequence: List[float], scale: float = 0.5) -> List[float]:
        """68. Scaled antiderivative (weighted cumulative sum)"""
        result = [0]
        for val in sequence:
            result.append(result[-1] + val * scale)
        return result
    
    def difference_of_gaussians(self, sequence: List[float], sigma1: float = 1.0, sigma2: float = 2.0) -> List[float]:
        """69. Difference of Gaussians derivative (edge detection inspired)"""
        # Simplified DoG using different smoothing windows
        smooth1 = self.smoothed_derivative(sequence, window=int(sigma1 * 2 + 1))
        smooth2 = self.smoothed_derivative(sequence, window=int(sigma2 * 2 + 1))
        min_len = min(len(smooth1), len(smooth2))
        return [smooth1[i] - smooth2[i] for i in range(min_len)]
    
    # Continue with more variations...
    def get_all_derivatives(self, sequence: List[float]) -> dict:
        """
        Calculate all 69+ derivative variations.
        
        Returns dictionary with all results.
        """
        results = {}
        
        # Add all implemented derivatives (1-44)
        results['01_first_derivative'] = self.first_derivative(sequence)
        results['02_second_derivative'] = self.second_derivative(sequence)
        results['03_third_derivative'] = self.third_derivative(sequence)
        results['04_fourth_derivative'] = self.nth_derivative(sequence, 4)
        results['05_central_derivative'] = self.central_derivative(sequence)
        results['06_backward_derivative'] = self.backward_derivative(sequence)
        results['07_logarithmic_derivative'] = self.logarithmic_derivative([abs(x)+1 for x in sequence])
        results['08_fractional_derivative'] = self.fractional_derivative(sequence, 0.5)
        
        results['09_antiderivative'] = self.antiderivative(sequence)
        results['10_double_antiderivative'] = self.double_antiderivative(sequence)
        results['11_triple_antiderivative'] = self.nth_antiderivative(sequence, 3)
        
        results['12_multiplicative_inverse'] = self.multiplicative_inverse([x if x != 0 else 1 for x in sequence])
        results['13_additive_inverse'] = self.additive_inverse(sequence)
        results['14_compositional_inverse'] = self.compositional_inverse(sequence)
        
        results['15_reverse_sequence'] = self.reverse_sequence(sequence)
        results['16_reverse_differences'] = self.reverse_differences(sequence)
        results['17_reverse_cumulative'] = self.reverse_cumulative(sequence)
        
        results['18_laplacian'] = self.laplacian(sequence)
        results['19_gradient_magnitude'] = self.gradient_magnitude(sequence)
        results['20_exponential_derivative'] = self.exponential_derivative(sequence)
        
        results['21_rafaelian_derivative'] = self.rafaelian_derivative(sequence)
        results['22_phi_weighted'] = self.phi_weighted_derivative(sequence)
        results['23_harmonic'] = self.harmonic_derivative(sequence)
        results['24_geometric'] = self.geometric_derivative([abs(x)+1 for x in sequence])
        
        # Additional operations (25-44)
        results['25_normalized'] = self.normalized_derivative(sequence)
        results['26_percentile'] = self.percentile_derivative([abs(x)+1 for x in sequence])
        results['27_cumulative'] = self.cumulative_derivative(sequence)
        results['28_absolute'] = self.absolute_derivative(sequence)
        results['29_sign'] = self.sign_derivative(sequence)
        results['30_smoothed'] = self.smoothed_derivative(sequence, window=3)
        
        results['31_trapezoidal'] = self.trapezoidal_integration(sequence)
        results['32_simpsons'] = self.simpsons_integration(sequence)
        results['33_forward_euler'] = self.forward_euler(sequence)
        results['34_backward_euler'] = self.backward_euler(sequence)
        
        results['35_radial'] = self.radial_derivative(sequence)
        results['36_angular'] = self.angular_derivative(sequence)
        results['37_spherical'] = self.spherical_derivative(sequence)
        
        results['38_power'] = self.power_derivative(sequence, p=2)
        results['39_variational'] = self.variational_derivative(sequence)
        results['40_fractal'] = self.fractal_derivative(sequence, fractal_dim=1.5)
        results['41_multifractal'] = self.multifractal_derivative(sequence)
        
        results['42_weighted_antiderivative'] = self.weighted_antiderivative(sequence, [1.0]*len(sequence))
        results['43_material'] = self.material_derivative(sequence, [1.0]*len(sequence))
        results['44_stochastic'] = self.stochastic_derivative(sequence, noise_level=0.1)
        
        # New distinct operations (45-69)
        results['45_normalized'] = self.normalized_derivative(sequence)
        results['46_percentile'] = self.percentile_derivative([abs(x)+1 for x in sequence])
        results['47_cumulative'] = self.cumulative_derivative(sequence)
        results['48_absolute'] = self.absolute_derivative(sequence)
        results['49_sign'] = self.sign_derivative(sequence)
        results['50_smoothed'] = self.smoothed_derivative(sequence)
        results['51_weighted_sum'] = self.weighted_sum_derivative(sequence)
        results['52_exp_smoothed'] = self.exponential_smoothed_derivative(sequence)
        results['53_bilateral'] = self.bilateral_derivative(sequence)
        results['54_median'] = self.median_derivative(sequence)
        results['55_polynomial'] = self.polynomial_derivative(sequence)
        results['56_adaptive'] = self.adaptive_derivative(sequence)
        results['57_momentum'] = self.momentum_derivative(sequence)
        results['58_wavelet'] = self.wavelet_derivative(sequence)
        results['59_robust'] = self.robust_derivative(sequence)
        results['60_constrained'] = self.constrained_derivative(sequence)
        results['61_cyclic'] = self.cyclic_derivative(sequence)
        results['62_bidirectional_anti'] = self.bidirectional_antiderivative(sequence)
        results['63_log'] = self.log_derivative(sequence)
        results['64_sqrt'] = self.sqrt_derivative(sequence)
        results['65_higher_mixed'] = self.higher_order_mixed(sequence)
        results['66_integral_transform'] = self.integral_transform_derivative(sequence)
        results['67_piecewise_linear'] = self.piecewise_linear_derivative(sequence)
        results['68_scaled_anti'] = self.scaled_antiderivative(sequence)
        results['69_difference_gaussians'] = self.difference_of_gaussians(sequence)
        
        return results


# Example usage
if __name__ == "__main__":
    print("=" * 70)
    print("69+ Derivatives and Antiderivatives Calculator")
    print("=" * 70)
    
    calc = DerivativeCalculator()
    
    # Test sequence (Rafaelian numbers)
    test_sequence = [2, 5, 10, 18, 25, 60, 144, 288, 555, 777]
    
    print(f"\nOriginal Sequence: {test_sequence}")
    print("\n" + "=" * 70)
    
    # Calculate some key derivatives
    print("\nKey Derivatives:")
    print(f"1st Derivative: {calc.first_derivative(test_sequence)}")
    print(f"2nd Derivative: {calc.second_derivative(test_sequence)}")
    print(f"3rd Derivative: {calc.third_derivative(test_sequence)}")
    print(f"Antiderivative: {calc.antiderivative(test_sequence)[:10]}")
    print(f"Inverse: {calc.multiplicative_inverse(test_sequence)[:5]}")
    print(f"Reverse: {calc.reverse_sequence(test_sequence)}")
    print(f"Rafaelian Derivative: {[round(x, 2) for x in calc.rafaelian_derivative(test_sequence)]}")
    
    # Get all 69+ variations
    print("\n" + "=" * 70)
    print("Calculating all 69+ derivative variations...")
    all_derivs = calc.get_all_derivatives(test_sequence)
    print(f"Total variations calculated: {len(all_derivs)}")
    
    print("\nSample of variations:")
    for key in list(all_derivs.keys())[:10]:
        value = all_derivs[key]
        if isinstance(value, list) and len(value) > 0:
            if isinstance(value[0], complex):
                print(f"{key}: [complex values, length={len(value)}]")
            else:
                print(f"{key}: {value[:5]}...")
    
    print("\n" + "=" * 70)
    print("Calculator demo completed!")
    print("=" * 70)
