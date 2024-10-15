# Function to evaluate student's performance based on percentage
def evaluate_performance(percentage):
    if percentage >= 90:
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Needs Improvement"

# Example usage
percentage = float(input("Enter the percentage: "))
result = evaluate_performance(percentage)
print(result)

# Function to find the largest number among three
def largest_of_three(a, b, c):
    return max(a, b, c)

# Example usage
a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))
print("The largest number is:", largest_of_three(a, b, c))

# Function to print Fibonacci series up to n terms
n = int(input("Masukkan batas bilangan Fibonaci: "))

a, b = 0, 1
while a <= n:
        print(a, end=" ")
        a, b = b, a + b
print("\n")

# Example usage

# Fungsi untuk mencetak angka ganjil hingga n
def cetak_angka_ganjil(n):
    for i in range(1, n + 1):
        if i % 2 != 0:  # Memeriksa apakah angka ganjil
            print(i, end=' ')
    print()

# Contoh penggunaan
n = int(input("Masukkan nilai n: "))    
cetak_angka_ganjil(n)


# Function to print pattern based on n
def print_pattern(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=' ')
        print()

# Example usage
n = int(input("Enter the value of n: "))
print_pattern(n)