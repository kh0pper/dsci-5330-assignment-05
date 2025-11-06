#!/usr/bin/env python3
"""
Ford Motor Company Operations Strategy Visualizations
Generate comprehensive charts for Assignment 05 memorandum
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np
import pandas as pd
import seaborn as sns
from datetime import datetime

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (14, 8)
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 11

# Create output directory reference
output_dir = '/home/kh0pp/DSCI-5330/assignment-05/visualizations/'

# ============================================================================
# VISUALIZATION 1: Business Unit Financial Performance Dashboard (2024)
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Ford Motor Company Business Unit Performance Dashboard (2024)',
             fontsize=16, fontweight='bold', y=0.995)

# Data for business units
business_units = ['Ford Blue', 'Ford Model e', 'Ford Pro']
wholesale_units = [2279, 3861, 1503]  # in thousands
revenue = [72.819, 3.861, 66.906]  # in billions
ebit = [9.328, -5.076, 9.015]  # in billions
ebit_margin = [12.8, -131.8, 13.5]  # in percent

colors_units = ['#0066CC', '#FF6600', '#00AA00']

# 1. Wholesale Units by Business Unit
ax = axes[0, 0]
bars = ax.bar(business_units, wholesale_units, color=colors_units, alpha=0.8, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Wholesale Units (thousands)', fontsize=11, fontweight='bold')
ax.set_title('A. Annual Wholesale Units (2024)', fontsize=12, fontweight='bold')
ax.set_ylim(0, 3500)
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(height):,}K',
            ha='center', va='bottom', fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# 2. Revenue by Business Unit
ax = axes[0, 1]
bars = ax.bar(business_units, revenue, color=colors_units, alpha=0.8, edgecolor='black', linewidth=1.5)
ax.set_ylabel('Revenue ($ Billions)', fontsize=11, fontweight='bold')
ax.set_title('B. Total Revenue (2024)', fontsize=12, fontweight='bold')
ax.set_ylim(0, 80)
for i, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'${height:.1f}B',
            ha='center', va='bottom', fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# 3. EBIT by Business Unit
ax = axes[1, 0]
bars = ax.bar(business_units, ebit, color=colors_units, alpha=0.8, edgecolor='black', linewidth=1.5)
ax.set_ylabel('EBIT ($ Billions)', fontsize=11, fontweight='bold')
ax.set_title('C. Operating Income (EBIT) 2024', fontsize=12, fontweight='bold')
ax.axhline(y=0, color='black', linestyle='-', linewidth=2)
ax.set_ylim(-8, 12)
for i, bar in enumerate(bars):
    height = bar.get_height()
    va_pos = 'bottom' if height >= 0 else 'top'
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'${height:.1f}B',
            ha='center', va=va_pos, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

# 4. EBIT Margin by Business Unit
ax = axes[1, 1]
colors_margin = ['green' if m > 0 else 'red' for m in ebit_margin]
bars = ax.bar(business_units, ebit_margin, color=colors_margin, alpha=0.7, edgecolor='black', linewidth=1.5)
ax.set_ylabel('EBIT Margin (%)', fontsize=11, fontweight='bold')
ax.set_title('D. Operating Margin (EBIT Margin) 2024', fontsize=12, fontweight='bold')
ax.axhline(y=0, color='black', linestyle='-', linewidth=2)
ax.set_ylim(-150, 20)
for i, bar in enumerate(bars):
    height = bar.get_height()
    va_pos = 'bottom' if height >= 0 else 'top'
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{height:.1f}%',
            ha='center', va=va_pos, fontweight='bold')
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig(output_dir + '01_business_unit_performance_dashboard.png', dpi=300, bbox_inches='tight')
print("✓ Created: Business Unit Performance Dashboard")
plt.close()

# ============================================================================
# VISUALIZATION 2: Manufacturing Footprint and Specialization
# ============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
fig.suptitle('Ford Manufacturing Footprint and Strategic Specialization',
             fontsize=16, fontweight='bold')

# Left: Global Facilities by Region
regions = ['North America\n(15 plants)', 'Europe\n(8 plants)', 'Asia-Pacific\n(12 plants)',
           'Joint Ventures\n(6 JV partners)']
facility_counts = [15, 8, 12, 6]
region_colors = ['#0066CC', '#FF6600', '#00AA00', '#9900CC']

ax = ax1
wedges, texts, autotexts = ax.pie(facility_counts, labels=regions, autopct='%1.1f%%',
                                    colors=region_colors, startangle=90,
                                    textprops={'fontsize': 11, 'fontweight': 'bold'})
ax.set_title('Geographic Distribution of 41 Manufacturing Plants', fontsize=12, fontweight='bold')
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Right: Specialization by Business Unit
ax = ax2
business_units_spec = ['Ford Blue\n(ICE)', 'Ford Model e\n(EV)', 'Ford Pro\n(Commercial)']
plant_focus = [18, 8, 15]  # approximate allocation
colors_spec = ['#0066CC', '#FF6600', '#00AA00']

bars = ax.barh(business_units_spec, plant_focus, color=colors_spec, alpha=0.8, edgecolor='black', linewidth=1.5)
ax.set_xlabel('Manufacturing Plants by Specialization', fontsize=11, fontweight='bold')
ax.set_title('Strategic Specialization by Business Unit', fontsize=12, fontweight='bold')
ax.set_xlim(0, 20)

for i, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width, bar.get_y() + bar.get_height()/2.,
            f'{int(width)} plants',
            ha='left', va='center', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig(output_dir + '02_manufacturing_footprint.png', dpi=300, bbox_inches='tight')
print("✓ Created: Manufacturing Footprint")
plt.close()

# ============================================================================
# VISUALIZATION 3: Capacity Utilization Trends (2015-2024)
# ============================================================================

fig, ax = plt.subplots(figsize=(14, 8))

years = [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
ice_capacity_util = [88, 85, 82, 75, 78, 65, 82, 78, 70, 65]  # percentage
ev_capacity_util = [0, 0, 0, 5, 8, 12, 25, 35, 40, 42]  # percentage
total_units = [6.7, 6.8, 6.8, 5.4, 5.5, 4.2, 4.9, 4.2, 4.0, 4.3]  # millions

ax1 = ax
ax1.plot(years, ice_capacity_util, marker='o', linewidth=2.5, markersize=8,
         label='ICE Capacity Utilization', color='#0066CC')
ax1.plot(years, ev_capacity_util, marker='s', linewidth=2.5, markersize=8,
         label='EV Capacity Utilization', color='#FF6600')
ax1.set_xlabel('Year', fontsize=12, fontweight='bold')
ax1.set_ylabel('Capacity Utilization (%)', fontsize=12, fontweight='bold', color='black')
ax1.set_ylim(0, 100)
ax1.grid(True, alpha=0.3)
ax1.legend(loc='upper right', fontsize=11)

# Add secondary axis for production volume
ax2 = ax1.twinx()
ax2.plot(years, total_units, marker='^', linewidth=2.5, markersize=8,
         label='Total Production (Millions)', color='#00AA00', linestyle='--')
ax2.set_ylabel('Total Production Volume (Millions of Units)', fontsize=12, fontweight='bold', color='#00AA00')
ax2.set_ylim(0, 8)
ax2.legend(loc='center right', fontsize=11)

ax1.set_title('Ford Capacity Utilization Trends: ICE Decline and EV Ramp (2015-2024)',
              fontsize=14, fontweight='bold')
ax1.set_xticks(years)

plt.tight_layout()
plt.savefig(output_dir + '03_capacity_utilization_trends.png', dpi=300, bbox_inches='tight')
print("✓ Created: Capacity Utilization Trends")
plt.close()

# ============================================================================
# VISUALIZATION 4: Operations Decision Categories - Strategic Fit
# ============================================================================

fig, axes = plt.subplots(1, 3, figsize=(18, 8))
fig.suptitle('MIT Operations Decision Categories: Ford Strategic Fit Analysis',
             fontsize=16, fontweight='bold')

# Define decision categories and scores (1-5 scale)
decision_categories = ['Facilities\nLocationSpecialization', 'Capacity\nAmount & Timing',
                       'Vertical\nIntegration', 'Process\nTechnology', 'Workforce\nSkills',
                       'Supply\nChain']

# Ford Blue (Cost Leadership Strategy)
blue_scores = [4, 3, 3, 4, 3, 3]
blue_label = 'Ford Blue\n(Cost Leadership)'

# Ford Model e (Differentiation/Entry Strategy)
modele_scores = [3, 2, 4, 3, 2, 2]
modele_label = 'Ford Model e\n(Differentiation)'

# Ford Pro (Premium Services Strategy)
pro_scores = [4, 4, 4, 4, 4, 4]
pro_label = 'Ford Pro\n(Premium Services)'

x = np.arange(len(decision_categories))
width = 0.25

for idx, (ax, scores, label, color) in enumerate([(axes[0], blue_scores, blue_label, '#0066CC'),
                                                    (axes[1], modele_scores, modele_label, '#FF6600'),
                                                    (axes[2], pro_scores, pro_label, '#00AA00')]):
    bars = ax.bar(x, scores, width=0.6, color=color, alpha=0.8, edgecolor='black', linewidth=1.5)
    ax.set_ylabel('Alignment Score (1=Weak, 5=Strong)', fontsize=10, fontweight='bold')
    ax.set_title(label, fontsize=12, fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(decision_categories, fontsize=9)
    ax.set_ylim(0, 5.5)
    ax.axhline(y=3.5, color='green', linestyle='--', linewidth=1, alpha=0.5, label='Strong Alignment')
    ax.grid(axis='y', alpha=0.3)

    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height)}',
                ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.tight_layout()
plt.savefig(output_dir + '04_operations_decision_categories.png', dpi=300, bbox_inches='tight')
print("✓ Created: Operations Decision Categories")
plt.close()

# ============================================================================
# VISUALIZATION 5: Vertical Integration Timeline - Battery Strategy
# ============================================================================

fig, ax = plt.subplots(figsize=(16, 8))

# Timeline data
events = [
    ('2018', 'EV Strategy\nAnnounced', 'strategy'),
    ('2019', 'Model e\nUnit Created', 'strategy'),
    ('2020', 'Ford+\nPlan Launched', 'strategy'),
    ('2021', 'BlueOval SK\nAnnounced', 'partnership'),
    ('2022', 'Battery Plant\nConstruction Begins', 'construction'),
    ('2023', 'First Batteries\nBegin Production', 'production'),
    ('2024', 'Ramping\nProduction', 'production'),
    ('2025-2026', 'Target Full\nCapacity', 'target'),
]

years_numeric = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025.5]
colors_timeline = {
    'strategy': '#0066CC',
    'partnership': '#9900CC',
    'construction': '#FF6600',
    'production': '#00AA00',
    'target': '#CCCCCC'
}

# Draw timeline
ax.plot([2018, 2025.5], [0, 0], 'k-', linewidth=3)

# Add events
for year, event, event_type in events:
    y_pos = 1 if events.index((year, event, event_type)) % 2 == 0 else -1
    color = colors_timeline[event_type]

    ax.scatter(float(year.split('-')[0]) if '-' not in year else 2025.5, 0,
              s=300, c=color, zorder=3, edgecolor='black', linewidth=2)
    ax.plot([float(year.split('-')[0]) if '-' not in year else 2025.5,
             float(year.split('-')[0]) if '-' not in year else 2025.5],
           [0, y_pos*0.5], 'k-', linewidth=1.5)

    ax.text(float(year.split('-')[0]) if '-' not in year else 2025.5,
           y_pos*1.2, event, ha='center', fontsize=10, fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.5', facecolor=color, alpha=0.7, edgecolor='black'))

# Legend
legend_elements = [
    mpatches.Patch(facecolor='#0066CC', edgecolor='black', label='Strategic Decision'),
    mpatches.Patch(facecolor='#9900CC', edgecolor='black', label='Partnership'),
    mpatches.Patch(facecolor='#FF6600', edgecolor='black', label='Infrastructure Build'),
    mpatches.Patch(facecolor='#00AA00', edgecolor='black', label='Production Phase'),
    mpatches.Patch(facecolor='#CCCCCC', edgecolor='black', label='Target State'),
]
ax.legend(handles=legend_elements, loc='lower center', ncol=5, fontsize=10, frameon=True)

ax.set_xlim(2017.5, 2026)
ax.set_ylim(-2, 2)
ax.set_xticks(range(2018, 2026))
ax.set_xticklabels(range(2018, 2026), fontsize=11, fontweight='bold')
ax.set_yticks([])
ax.spines['left'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_title('Ford Battery Vertical Integration Strategy Timeline (2018-2026)',
            fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig(output_dir + '05_vertical_integration_timeline.png', dpi=300, bbox_inches='tight')
print("✓ Created: Vertical Integration Timeline")
plt.close()

# ============================================================================
# VISUALIZATION 6: Strategic Fit and Effectiveness Matrix
# ============================================================================

fig, ax = plt.subplots(figsize=(12, 10))

# Create 2x2 matrix: Strategic Alignment vs Implementation Effectiveness
business_units_matrix = ['Ford Blue', 'Ford Model e', 'Ford Pro']
strategic_alignment = [4.2, 3.0, 4.5]  # scores out of 5
implementation_effectiveness = [4.0, 2.5, 4.3]  # scores out of 5
unit_sizes = [2279*3, 3861*3, 1503*3]  # proportional to revenue/units

colors_matrix = ['#0066CC', '#FF6600', '#00AA00']

# Scatter plot with sized bubbles
for i, (unit, align, impl, size, color) in enumerate(
    zip(business_units_matrix, strategic_alignment, implementation_effectiveness, unit_sizes, colors_matrix)):
    ax.scatter(align, impl, s=size, c=color, alpha=0.6, edgecolor='black', linewidth=2.5)
    ax.text(align, impl, unit, ha='center', va='center', fontsize=11, fontweight='bold')

# Add quadrant lines
ax.axhline(y=3.5, color='gray', linestyle='--', linewidth=2, alpha=0.5)
ax.axvline(x=3.5, color='gray', linestyle='--', linewidth=2, alpha=0.5)

# Add quadrant labels
ax.text(2.2, 4.8, 'Low Alignment\nHigh Effectiveness', fontsize=10,
       bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3), ha='center')
ax.text(4.8, 4.8, 'High Alignment\nHigh Effectiveness\n(IDEAL)', fontsize=10,
       bbox=dict(boxstyle='round', facecolor='green', alpha=0.3), ha='center', fontweight='bold')
ax.text(2.2, 2.2, 'Low Alignment\nLow Effectiveness\n(CHALLENGE)', fontsize=10,
       bbox=dict(boxstyle='round', facecolor='red', alpha=0.3), ha='center', fontweight='bold')
ax.text(4.8, 2.2, 'High Alignment\nLow Effectiveness', fontsize=10,
       bbox=dict(boxstyle='round', facecolor='orange', alpha=0.3), ha='center')

ax.set_xlabel('Strategic Alignment (Operations supports Strategy) →', fontsize=12, fontweight='bold')
ax.set_ylabel('Implementation Effectiveness (Execution Quality) →', fontsize=12, fontweight='bold')
ax.set_xlim(2, 5)
ax.set_ylim(2, 5)
ax.set_xticks([2.5, 3.5, 4.5])
ax.set_yticks([2.5, 3.5, 4.5])
ax.grid(True, alpha=0.2)

ax.set_title('Ford Business Units: Strategic-Operational Alignment vs Implementation Effectiveness',
            fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(output_dir + '06_strategic_fit_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Created: Strategic Fit and Effectiveness Matrix")
plt.close()

# ============================================================================
# Print completion summary
# ============================================================================

print("\n" + "="*70)
print("FORD MOTOR COMPANY VISUALIZATIONS CREATED SUCCESSFULLY")
print("="*70)
print(f"\nOutput Directory: {output_dir}")
print("\nVisualizations Created:")
print("  1. Business Unit Performance Dashboard (2024)")
print("  2. Manufacturing Footprint and Specialization")
print("  3. Capacity Utilization Trends (2015-2024)")
print("  4. Operations Decision Categories - Strategic Fit")
print("  5. Vertical Integration Timeline (Battery Strategy)")
print("  6. Strategic Fit and Effectiveness Matrix")
print("\nAll visualizations saved as high-resolution PNG files (300 DPI)")
print("Ready for embedding in memorandum")
print("="*70 + "\n")
