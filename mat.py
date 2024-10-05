import matplotlib.pyplot as plt

# Group by 'PROVINCIA' and sum the 'PROBADA' values
reserves_by_province = data.groupby('PROVINCIA')['PROBADA'].sum().reset_index()

# Plot a bar chart of 'PROVINCIA' vs 'PROBADA'
plt.figure(figsize=(10, 6))
plt.bar(reserves_by_province['PROVINCIA'], reserves_by_province['PROBADA'])

# Customize the chart
plt.xticks(rotation=90)
plt.xlabel('Provincia')
plt.ylabel('Reservas Probadas (en onzas)')
plt.title('Reservas Probadas de Oro por Provincia')
plt.tight_layout()

# Show the plot
plt.show()