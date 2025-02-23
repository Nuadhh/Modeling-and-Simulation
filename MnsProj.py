# Simulation: Saving for a PS5
import matplotlib.pyplot as plt


salary_per_half_month = 10000  
tuition_fee = 4000  
general_expenses = 5000  
ps5_cost = 30000  
savings_per_half_month = salary_per_half_month - (tuition_fee + general_expenses)
savings_per_month = savings_per_half_month * 2  

# Simulation
total_savings = 0
months = 0
savings_progress = []

while total_savings < ps5_cost:
    total_savings += savings_per_month
    months += 1
    savings_progress.append(total_savings)
    print(f"Month {months}: Savings = {total_savings} PHP")

# Visualization
plt.plot(range(1, months + 1), savings_progress, marker='o', linestyle='-')
plt.xlabel('Months')
plt.ylabel('Total Savings (PHP)')
plt.title('Savings Progress Towards a PS5')
plt.grid()
plt.show()

print(f"\nYou can afford a PS5 in {months} months.")