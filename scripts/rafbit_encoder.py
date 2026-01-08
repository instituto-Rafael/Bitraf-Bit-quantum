#!/usr/bin/env python3
"""
RafBit Encoder/Decoder
======================

Implementation of Bitraf (RafBit) encoding - a 10-state quantum bit with dual parity.

Author: Rafael Melo Reis
Date: January 2026
License: MIT
"""

from typing import List, Tuple
import numpy as np


class RafBit:
    """
    Represents a single RafBit with 10 base states and dual parity.
    
    States: {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    Parities: {+, -}
    Total capacity: 20 states per RafBit
    """
    
    STATES = 10
    PARITIES = 2
    TOTAL_CAPACITY = STATES * PARITIES
    
    def __init__(self, state: int, parity: int = 1):
        """
        Initialize a RafBit.
        
        Args:
            state: Integer from 0-9 representing the base state
            parity: +1 (positive) or -1 (negative)
        """
        if not 0 <= state < self.STATES:
            raise ValueError(f"State must be between 0 and {self.STATES-1}")
        if parity not in [1, -1]:
            raise ValueError("Parity must be +1 or -1")
        
        self.state = state
        self.parity = parity
    
    def to_int(self) -> int:
        """Convert RafBit to integer representation (0-19)."""
        return self.state * 2 + (0 if self.parity == 1 else 1)
    
    @classmethod
    def from_int(cls, value: int) -> 'RafBit':
        """Create RafBit from integer (0-19)."""
        if not 0 <= value < cls.TOTAL_CAPACITY:
            raise ValueError(f"Value must be between 0 and {cls.TOTAL_CAPACITY-1}")
        state = value // 2
        parity = 1 if value % 2 == 0 else -1
        return cls(state, parity)
    
    def __repr__(self) -> str:
        parity_symbol = '+' if self.parity == 1 else '-'
        return f"RafBit({self.state}{parity_symbol})"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, RafBit):
            return False
        return self.state == other.state and self.parity == other.parity


class RafBitEncoder:
    """
    Encoder/Decoder for converting text and data to/from RafBit representation.
    """
    
    def __init__(self):
        self.rafbit_class = RafBit
    
    def encode_byte(self, byte: int) -> List[RafBit]:
        """
        Encode a single byte (0-255) into RafBits.
        Uses base-20 representation.
        
        Args:
            byte: Integer from 0-255
            
        Returns:
            List of RafBits representing the byte
        """
        if not 0 <= byte <= 255:
            raise ValueError("Byte must be between 0 and 255")
        
        # Convert to base-20 (requires 2 RafBits for 0-255)
        # 20^2 = 400 > 255, so 2 RafBits are sufficient
        rafbits = []
        remainder = byte
        
        # First RafBit (least significant)
        rafbits.append(RafBit.from_int(remainder % 20))
        remainder //= 20
        
        # Second RafBit (most significant)
        rafbits.append(RafBit.from_int(remainder % 20))
        
        return rafbits
    
    def decode_byte(self, rafbits: List[RafBit]) -> int:
        """
        Decode RafBits back to a byte.
        
        Args:
            rafbits: List of 2 RafBits
            
        Returns:
            Original byte value (0-255)
        """
        if len(rafbits) != 2:
            raise ValueError("Need exactly 2 RafBits to decode a byte")
        
        # Convert from base-20
        byte_value = rafbits[0].to_int() + rafbits[1].to_int() * 20
        
        if byte_value > 255:
            raise ValueError("Invalid RafBit encoding for byte")
        
        return byte_value
    
    def encode_string(self, text: str) -> List[RafBit]:
        """
        Encode a string into RafBits using UTF-8.
        
        Args:
            text: String to encode
            
        Returns:
            List of RafBits representing the string
        """
        byte_array = text.encode('utf-8')
        rafbits = []
        
        for byte in byte_array:
            rafbits.extend(self.encode_byte(byte))
        
        return rafbits
    
    def decode_string(self, rafbits: List[RafBit]) -> str:
        """
        Decode RafBits back to a string.
        
        Args:
            rafbits: List of RafBits (must have even length)
            
        Returns:
            Decoded string
        """
        if len(rafbits) % 2 != 0:
            raise ValueError("RafBit list must have even length for string decoding")
        
        byte_array = []
        for i in range(0, len(rafbits), 2):
            byte_value = self.decode_byte(rafbits[i:i+2])
            byte_array.append(byte_value)
        
        return bytes(byte_array).decode('utf-8')
    
    def encode_number(self, number: int) -> List[RafBit]:
        """
        Encode an integer into RafBits using base-20.
        
        Args:
            number: Non-negative integer
            
        Returns:
            List of RafBits
        """
        if number < 0:
            raise ValueError("Number must be non-negative")
        
        if number == 0:
            return [RafBit.from_int(0)]
        
        rafbits = []
        while number > 0:
            rafbits.append(RafBit.from_int(number % 20))
            number //= 20
        
        return rafbits
    
    def decode_number(self, rafbits: List[RafBit]) -> int:
        """
        Decode RafBits back to an integer.
        
        Args:
            rafbits: List of RafBits
            
        Returns:
            Decoded integer
        """
        number = 0
        for i, rafbit in enumerate(rafbits):
            number += rafbit.to_int() * (20 ** i)
        
        return number
    
    def add_error_correction(self, rafbits: List[RafBit]) -> List[RafBit]:
        """
        Add Tag14 error correction to RafBit sequence.
        Implements simple parity-based error detection.
        
        Args:
            rafbits: Original RafBit sequence
            
        Returns:
            RafBits with error correction added
        """
        # Calculate checksum based on states and parities
        state_sum = sum(rb.state for rb in rafbits)
        parity_sum = sum(rb.parity for rb in rafbits)
        
        # Create two check RafBits
        check1 = RafBit(state_sum % 10, 1 if parity_sum >= 0 else -1)
        check2 = RafBit(len(rafbits) % 10, 1 if len(rafbits) % 2 == 0 else -1)
        
        return rafbits + [check1, check2]
    
    def verify_error_correction(self, rafbits: List[RafBit]) -> Tuple[bool, List[RafBit]]:
        """
        Verify and remove error correction from RafBit sequence.
        
        Args:
            rafbits: RafBit sequence with error correction
            
        Returns:
            Tuple of (is_valid, original_rafbits)
        """
        if len(rafbits) < 2:
            return False, rafbits
        
        # Extract check bits
        data_rafbits = rafbits[:-2]
        check1, check2 = rafbits[-2:]
        
        # Recalculate checksums
        state_sum = sum(rb.state for rb in data_rafbits)
        parity_sum = sum(rb.parity for rb in data_rafbits)
        
        expected_check1 = RafBit(state_sum % 10, 1 if parity_sum >= 0 else -1)
        expected_check2 = RafBit(len(data_rafbits) % 10, 1 if len(data_rafbits) % 2 == 0 else -1)
        
        is_valid = (check1 == expected_check1) and (check2 == expected_check2)
        
        return is_valid, data_rafbits


def calculate_capacity(n_rafbits: int) -> int:
    """
    Calculate total capacity for n RafBits.
    
    Args:
        n_rafbits: Number of RafBits
        
    Returns:
        Total number of unique states
    """
    return RafBit.TOTAL_CAPACITY ** n_rafbits


def compare_to_binary(n_bits: int) -> dict:
    """
    Compare RafBit capacity to binary bits.
    
    Args:
        n_bits: Number of bits to compare
        
    Returns:
        Dictionary with comparison data
    """
    binary_capacity = 2 ** n_bits
    rafbit_capacity = calculate_capacity(n_bits)
    
    return {
        'n_bits': n_bits,
        'binary_capacity': binary_capacity,
        'rafbit_capacity': rafbit_capacity,
        'ratio': rafbit_capacity / binary_capacity,
        'advantage': f"{rafbit_capacity / binary_capacity:.2f}x"
    }


# Example usage and tests
if __name__ == "__main__":
    print("=" * 60)
    print("RafBit Encoder/Decoder Demo")
    print("=" * 60)
    
    # Initialize encoder
    encoder = RafBitEncoder()
    
    # Test 1: Encode and decode a string
    print("\n1. String Encoding Test:")
    original_text = "RAFAELIA"
    print(f"   Original: {original_text}")
    
    encoded = encoder.encode_string(original_text)
    print(f"   Encoded: {encoded[:10]}... ({len(encoded)} RafBits)")
    
    decoded = encoder.decode_string(encoded)
    print(f"   Decoded: {decoded}")
    print(f"   Match: {original_text == decoded}")
    
    # Test 2: Encode and decode a number
    print("\n2. Number Encoding Test:")
    original_number = 12345
    print(f"   Original: {original_number}")
    
    encoded_num = encoder.encode_number(original_number)
    print(f"   Encoded: {encoded_num}")
    
    decoded_num = encoder.decode_number(encoded_num)
    print(f"   Decoded: {decoded_num}")
    print(f"   Match: {original_number == decoded_num}")
    
    # Test 3: Error correction
    print("\n3. Error Correction Test:")
    test_rafbits = encoder.encode_string("Test")
    print(f"   Original RafBits: {len(test_rafbits)}")
    
    with_ecc = encoder.add_error_correction(test_rafbits)
    print(f"   With ECC: {len(with_ecc)} RafBits")
    
    is_valid, recovered = encoder.verify_error_correction(with_ecc)
    print(f"   Validation: {is_valid}")
    print(f"   Recovered: {encoder.decode_string(recovered)}")
    
    # Test 4: Capacity comparison
    print("\n4. Capacity Comparison (RafBit vs Binary):")
    for n in [1, 2, 5, 10, 20]:
        comparison = compare_to_binary(n)
        print(f"   {n} bits:")
        print(f"      Binary: {comparison['binary_capacity']:,}")
        print(f"      RafBit: {comparison['rafbit_capacity']:,}")
        print(f"      Advantage: {comparison['advantage']}")
    
    print("\n" + "=" * 60)
    print("Demo completed successfully!")
    print("=" * 60)
