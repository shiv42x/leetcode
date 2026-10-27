class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        is_positive = (dividend > 0) == (divisor > 0)

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        quotient = 0

        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1

            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1

            abs_dividend -= temp_divisor
            quotient += multiple

        return quotient if is_positive else -quotient