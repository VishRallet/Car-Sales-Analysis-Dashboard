import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv("car_sales_financial_data_2022_2024.csv")

# Set the style and color palette
sns.set(style="whitegrid")
color_palette = sns.color_palette("pastel")

# 1. Multiple Bar Graph for Sales Comparison by Year
def sales_comparison_bar():
    plt.figure(figsize=(10, 6))
    bar_width = 0.25
    brands = df['Brand']
    sales_2022 = df['2022 Sales (millions)']
    sales_2023 = df['2023 Sales (millions)']
    sales_2024 = df['2024 Sales (millions)']

    # Bar positions
    r1 = range(len(brands))
    r2 = [x + bar_width for x in r1]
    r3 = [x + bar_width for x in r2]

    # Plot bars with a pastel color palette
    plt.bar(r1, sales_2022, color=color_palette[0], width=bar_width, edgecolor='grey', label='2022')
    plt.bar(r2, sales_2023, color=color_palette[1], width=bar_width, edgecolor='grey', label='2023')
    plt.bar(r3, sales_2024, color=color_palette[2], width=bar_width, edgecolor='grey', label='2024')

    # Label and legend
    plt.xlabel('Brand', fontweight='bold')
    plt.ylabel('Sales (millions)', fontweight='bold')
    plt.title('Car Sales Comparison (2022-2024)', fontweight='bold', fontsize=14)
    plt.xticks([r + bar_width for r in range(len(brands))], brands, rotation=45, fontsize=10)
    plt.legend()
    plt.tight_layout()
    plt.show()

# 2. Pie Chart for Revenue Distribution in 2024
def revenue_pie_chart():
    plt.figure(figsize=(8, 8))
    revenue_2024 = df['2024 Revenue (USD billion)']
    brands = df['Brand']

    plt.pie(revenue_2024, labels=brands, autopct='%1.1f%%', startangle=140, colors=color_palette, textprops={'fontsize': 10})
    plt.title('Revenue Distribution by Brand in 2024', fontweight='bold', fontsize=14)
    plt.show()

# 3. Line Chart for Net Profit Trends Over Years
def net_profit_line_chart():
    plt.figure(figsize=(10, 6))
    brands = df['Brand']
    profit_2022 = df['2022 Net Profit (USD billion)']
    profit_2023 = df['2023 Net Profit (USD billion)']
    profit_2024 = df['2024 Net Profit (USD billion)']

    # Plot lines with distinct colors and markers
    for i, brand in enumerate(brands):
        plt.plot([2022, 2023, 2024], [profit_2022[i], profit_2023[i], profit_2024[i]], marker='o', label=brand)

    # Label and legend
    plt.xlabel('Year', fontweight='bold')
    plt.ylabel('Net Profit (USD billion)', fontweight='bold')
    plt.title('Net Profit Trends (2022-2024)', fontweight='bold', fontsize=14)
    plt.legend(loc="upper left", fontsize=9)
    plt.tight_layout()
    plt.show()

# 4. Stacked Bar Chart for Revenue Comparison by Year
def revenue_stacked_bar_chart():
    plt.figure(figsize=(12, 6))
    brands = df['Brand']
    revenue_2022 = df['2022 Revenue (USD billion)']
    revenue_2023 = df['2023 Revenue (USD billion)']
    revenue_2024 = df['2024 Revenue (USD billion)']

    # Plot stacked bars with soft colors
    plt.bar(brands, revenue_2022, color=color_palette[0], label='2022')
    plt.bar(brands, revenue_2023, bottom=revenue_2022, color=color_palette[1], label='2023')
    plt.bar(brands, revenue_2024, bottom=[i+j for i,j in zip(revenue_2022, revenue_2023)], color=color_palette[2], label='2024')

    # Labels and legend
    plt.xlabel('Brand', fontweight='bold')
    plt.ylabel('Revenue (USD billion)', fontweight='bold')
    plt.title('Revenue Comparison (2022-2024)', fontweight='bold', fontsize=14)
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

# 5. Scatter Plot for Sales vs. Profit in 2024
def sales_vs_profit_scatter():
    plt.figure(figsize=(10, 6))
    sales_2024 = df['2024 Sales (millions)']
    profit_2024 = df['2024 Net Profit (USD billion)']
    brands = df['Brand']

    plt.scatter(sales_2024, profit_2024, color='purple', s=100, edgecolor='black', alpha=0.7)
    for i, brand in enumerate(brands):
        plt.text(sales_2024[i] + 0.1, profit_2024[i] + 0.1, brand, fontsize=9)

    plt.xlabel('Sales (millions)', fontweight='bold')
    plt.ylabel('Net Profit (USD billion)', fontweight='bold')
    plt.title('Sales vs. Profit in 2024', fontweight='bold', fontsize=14)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 6. Box Plot for Revenue Variability Across Years
def revenue_box_plot():
    plt.figure(figsize=(10, 6))
    data = [
        df['2022 Revenue (USD billion)'],
        df['2023 Revenue (USD billion)'],
        df['2024 Revenue (USD billion)']
    ]

    plt.boxplot(data, labels=['2022', '2023', '2024'], patch_artist=True, boxprops=dict(facecolor=color_palette[1], color="black"))
    plt.title('Revenue Variability Across Years', fontweight='bold', fontsize=14)
    plt.ylabel('Revenue (USD billion)')
    plt.grid(True)
    plt.show()

# Display the graphs
sales_comparison_bar()
revenue_pie_chart()
net_profit_line_chart()
revenue_stacked_bar_chart()
sales_vs_profit_scatter()
revenue_box_plot()
