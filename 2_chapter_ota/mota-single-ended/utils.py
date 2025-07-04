import pandas as pd
import numpy as np
from matplotlib import ticker
import matplotlib.pyplot as plt
import os
os.getcwd()
# helper function to process a line when converting a .txt file to a csv file
def process_line(line):
    parts = line.split()  # Splitting by space
    frequency = parts[0]
    magnitude, phase = parts[1].strip('(').strip('�)').split(',')  # Removing parentheses and splitting by comma
    magnitude = magnitude.strip('dB')
    
    return frequency, magnitude, phase
# function to convert a .txt file to a .csv file
def convert_to_csv(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    with open(output_file, 'w') as file:
        file.write('Frequency,Magnitude,Phase\n')  # Writing headers
        for line in lines:
            frequency, magnitude, phase = process_line(line)
            file.write(f'{frequency},{magnitude},{phase}\n')
# function to convert a .csv file to a pandas DataFrame
def list_to_df(data):
    df = pd.DataFrame({'Frequency': data[0], 'Magnitude': data[1], 'Phase': data[2]})
    return df
# function to convert a .txt file of LTspice magnitude/phase vs. frequency data to a pandas DataFrame
def spicetxtf_to_pd(input_files):
    dataframes = []
    for inputf in input_files:
        freq = []
        mag = []
        phase = []

        with open(inputf, 'r') as file:
            lines = file.readlines()
        for line in lines:
            frequency, magnitude, ph = process_line(line)
            freq.append(float(frequency))
            mag.append(float(magnitude))
            phase.append(float(ph))

        t = [freq, mag, phase]
        dataframes.append(list_to_df(t))
    return dataframes
# function to convert (frequency, magnitude, phase) .csv file to a pandas DataFrame
def scopycsvf_to_pd(csv_files):
    dataframes = []
    for file in csv_files:
        print(file)
        df = pd.read_csv(file, header=None)
        data_list = [df[col].tolist() for col in df.columns]
        data_df = pd.DataFrame({'Frequency': data_list[0], 'Magnitude': data_list[1], 'Phase': data_list[2]})
        dataframes.append(data_df)
    return dataframes
# function to compute the 3dB bandwidth from a pandas DataFrame
def compute_3db_bandwidth(df):
    # Compute the target magnitude as -3dB from the maximum data point
    target_magnitude = df['Magnitude'].max() - 3

    # Compute the absolute difference between each magnitude and the target magnitude
    diff = np.abs(df['Magnitude'] - target_magnitude)

    # Find the index of the minimum difference
    min_diff_index = diff.idxmin()

    # Return the frequency corresponding to the minimum difference
    return df['Frequency'].iloc[min_diff_index]
# function to compute the unity gain frequency from a pandas DataFrame
def compute_unity_gain_frequency(df):
    # Compute the absolute difference between each magnitude and 0dB
    diff = np.abs(df['Magnitude'] - 0)

    # Find the index of the minimum difference
    min_diff_index = diff.idxmin()

    # Return the frequency corresponding to the minimum difference
    return df['Frequency'].iloc[min_diff_index]
# function to compute the phase margin from a pandas DataFrame
def compute_phase_margin(df):
    # Compute the unity gain frequency
    unity_gain_freq = compute_unity_gain_frequency(df)

    # Find the phase at the unity gain frequency
    phase_at_unity_gain_freq = df.loc[df['Frequency'] == unity_gain_freq, 'Phase'].values[0]

    # Determine whether the initial phase is closer to 0 or 180
    initial_phase = df['Phase'].iloc[0]
    if abs(initial_phase - 0) < abs(initial_phase - 180):
        # If the initial phase is closer to 0, the phase margin is 180 minus the phase at the unity gain frequency
        phase_margin = 180 - abs(phase_at_unity_gain_freq)
    else:
        # If the initial phase is closer to 180, the phase margin is the phase at the unity gain frequency
        phase_margin = phase_at_unity_gain_freq
    phase_margin = phase_at_unity_gain_freq
    return phase_margin
# function to compute the dc gain from a pandas DataFrame
def compute_dc_gain(df):
    min_freq_row = df[df['Frequency'] == df['Frequency'].min()]
    dc_gain_db = df['Magnitude'].max()
    return dc_gain_db
# function to compute the stability parameters (3dB BW, phase-margin, unity gain freq, DC gain) from a pandas DataFrame
def stability_params(df):
    # Compute the 3dB bandwidth
    bandwidth_3db = compute_3db_bandwidth(df)

    # Compute the unity gain frequency
    unity_gain_freq = compute_unity_gain_frequency(df)

    # Compute the phase margin
    phase_margin = compute_phase_margin(df)
    
    # Compute the dc gain
    dc_gain = compute_dc_gain(df)

    return dc_gain, bandwidth_3db, unity_gain_freq, phase_margin
# function to plot the magnitude and phase response of a list of pandas DataFrames with their names as a legend
def plot_acresponse(dfs, names):
    fig, axs = plt.subplots(3, 1, figsize=(10, 15))

    min_freq = max(df['Frequency'].min() for df in dfs)  # Set min x-axis frequency to the max of the min frequencies
    max_freq = min(df['Frequency'].max() for df in dfs)  # Set max x-axis frequency to the min of the max frequencies

    min_mag = min(df[df['Frequency'].between(min_freq, max_freq)]['Magnitude'].min() for df in dfs) - 5  # Set min y-axis magnitude to the min of the magnitudes between min_freq and max_freq
    max_mag = max(df[df['Frequency'].between(min_freq, max_freq)]['Magnitude'].max() for df in dfs) + 5 # Set max y-axis magnitude to the max of the magnitudes between min_freq and max_freq

    min_phase = min(df[df['Frequency'].between(min_freq, max_freq)]['Phase'].min() for df in dfs) - 5  # Set min y-axis phase to the min of the phases between min_freq and max_freq
    max_phase = max(df[df['Frequency'].between(min_freq, max_freq)]['Phase'].max() for df in dfs) + 5 # Set max y-axis phase to the max of the phases between min_freq and max_freq
    
    # Initialize the table data
    table_data = []

    colors = []  # Store the colors of the plots

    for i, df in enumerate(dfs):  # Get the index and DataFrame
        df_name = names[i]  # Get the name from the names list

        mag_label = f'Magnitude ({df_name})'
        phase_label = f'Phase ({df_name})'

        line1, = axs[1].plot(df['Frequency'], df['Magnitude'], label=mag_label)  # Plot the magnitude
        axs[2].plot(df['Frequency'], df['Phase'], label=phase_label)  # Plot the phase

        colors.append(line1.get_color())  # Store the color of the plot

        # Compute the stability parameters
        dc_gain, bandwidth_3db, unity_gain_freq, phase_margin = stability_params(df)
        bandwidth_3db /= 1000  # Convert to kHz
        unity_gain_freq /= 1000  # Convert to kHz

        # Add the computations to the table data
        table_data.append([df_name, f"{dc_gain:.2f}", f"{bandwidth_3db:.2f}", f"{unity_gain_freq:.2f}", f"{phase_margin:.2f}"])

    # Create the table
    table = axs[0].table(cellText=table_data, colLabels=["Data Set","Adc (dB)", "BW 3dB (kHz)", "UGF (kHz)", "PM (degrees)"], loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)  # Increase the font size

    # Calculate the maximum length of the content in each column
    cellDict = table.get_celld()
    for i in range(len(table_data[0])):
        table.auto_set_column_width(i)

    # Bolden the labels and set the row colors
    cellDict[(0, 0)].set_fontsize(12)
    cellDict[(0, 0)].get_text().set_fontstyle('italic')
    cellDict[(0, 0)].get_text().set_horizontalalignment('center')
    for i in range(len(table_data[0])-1):
        cellDict[(0, i+1)].set_fontsize(12)
        cellDict[(0, i+1)].get_text().set_weight('560')
        cellDict[(0, i+1)].get_text().set_horizontalalignment('left')
    for i in range(len(table_data)):
        cellDict[(i+1, 0)].set_fontsize(12)
        cellDict[(i+1, 0)].get_text().set_weight('560')
        cellDict[(i+1, 0)].get_text().set_color(colors[i])  # Set the row color
        cellDict[(i+1, 0)].get_text().set_horizontalalignment('left')
        for j in range(1, len(table_data[0])):
            cellDict[(i+1, j)].set_fontsize(14)
            cellDict[(i+1, j)].get_text().set_weight('550')
            cellDict[(i+1, j)].get_text().set_color(colors[i])
            cellDict[(i+1, j)].get_text().set_horizontalalignment('center')
        
    table.scale(2, 3)  # Stretch the width of the table and increase the height of the rows

    axs[0].axis('off')  # Hide the axis and plot window of axs[0]

    axs[1].set_xscale('log')
    axs[2].set_xscale('log')

    axs[1].set_xlim(min_freq, max_freq)
    axs[2].set_xlim(min_freq, max_freq)
    
    axs[1].set_ylim(min_mag, max_mag)
    axs[2].set_ylim(min_phase, max_phase)

    for ax in axs[1:]:
        ax.grid(True, which='major', color='grey', linestyle='-')
        ax.xaxis.set_minor_locator(ticker.LogLocator(subs='all'))
        ax.grid(True, which='minor', color='lightgrey', linestyle=':')

    axs[1].set_xlabel('Frequency (Hz)')
    axs[1].set_ylabel('Magnitude (dB)')
    axs[1].legend()

    axs[2].set_xlabel('Frequency (Hz)')
    axs[2].set_ylabel('Phase (degrees)')
    axs[2].legend()

    plt.subplots_adjust(hspace=0.2)  # Adjust the space between subplots
    plt.show()
# function to read a .txt file (with headers and cols seperated by spaces) to a pandas DataFrame
def read_txt_to_df(file_path):
    df = pd.read_csv(file_path, sep="\s+", header=0)
    return df
# function to plot multiple x(t) vs vin(t) from pandas DataFrame; returns the indices of the vout vs. vin linear range bounds
def plotdf_x_vs_y_periodic(df, n, vin_col, vout_col, other_cols_groups=None):
    # Round Vin to 4 decimal places
    df['Vin_rounded'] = df[vin_col].round(4)

    # Find the index of the xth occurrence of Vin=0
    zero_indices = np.where(df['Vin_rounded'] == 0)[0]
    
    if len(zero_indices) < n:
        print(f"Not enough occurrences of Vin=0. Only found {len(zero_indices)} occurrences.")
        return

    start = zero_indices[n-1]

    # Find the index where Vin begins to decrease again
    vin_diff = df[vin_col].diff()
    decreasing_indices = np.where(vin_diff[start+1:] < 0)[0]

    if len(decreasing_indices) == 0:
        print("Vin does not begin to decrease after the xth occurrence of Vin=0.")
        return

    end = start + 1 + decreasing_indices[0]

    # Select the subset of the DataFrame between these indices and create a copy
    subset_df = df.iloc[start:end+1].copy()

    # Compute the derivative of Vout with respect to Vin
    subset_df['Gain'] = subset_df[vout_col].diff() / subset_df[vin_col].diff()

    # Find the region where the gain is approximately constant
    gain_diff = subset_df['Gain'].diff().abs()
    linear_region = gain_diff < 0.01  # Adjust this threshold as needed

    # Find the bounds that cover the maximum amount of consecutive linear data points
    linear_indices = subset_df[linear_region].index
    bounds = [linear_indices[0]]
    for i in range(1, len(linear_indices)):
        if linear_indices[i] - linear_indices[i-1] > 1:
            bounds.append(linear_indices[i])
    bounds.append(linear_indices[-1])

    # Choose the second as the lower bound and the last as the upper bound
    if len(bounds) >= 3:
        lower_bound = bounds[-2]
        upper_bound = bounds[-1]
    else:
        print("Not enough consecutive linear bounds.")
        return
    bound_indices = [lower_bound, upper_bound]
    
    # Plot Vout vs Vin for the subset of the DataFrame
    plt.figure(figsize=(20, 10))
    plt.plot(subset_df[vin_col], subset_df[vout_col], marker='o')

    # Draw vertical lines at the bounds of the linear region
    plt.axvline(x=subset_df.loc[lower_bound, vin_col], color='r', linestyle='--')
    plt.axvline(x=subset_df.loc[upper_bound, vin_col], color='r', linestyle='--')

    # Annotate the value of Vin at the bounds
    plt.annotate(f'Vin={subset_df.loc[lower_bound, vin_col]:.3f}', (subset_df.loc[lower_bound, vin_col], subset_df[vout_col].min()), textcoords="offset points", xytext=(10,-10), ha='left', color='red', fontsize=12)
    plt.annotate(f'Vin={subset_df.loc[upper_bound, vin_col]:.3f}', (subset_df.loc[upper_bound, vin_col], subset_df[vout_col].min()), textcoords="offset points", xytext=(10,-10), ha='left', color='red', fontsize=12)
    plt.annotate(f'Vout={subset_df.loc[lower_bound, vout_col]:.3f}', (subset_df.loc[lower_bound, vin_col], subset_df.loc[lower_bound, vout_col]), textcoords="offset points", xytext=(10,-10), ha='left', color='blue', fontsize=12)
    plt.annotate(f'Vout={subset_df.loc[upper_bound, vout_col]:.3f}', (subset_df.loc[upper_bound, vin_col], subset_df.loc[upper_bound,vout_col]), textcoords="offset points", xytext=(10,-10), ha='left', color='blue', fontsize=12)

    plt.title('Vout vs Vin')
    plt.xlabel('Vin')
    plt.ylabel('Vout')
    plt.grid(True)
    plt.show()

    # Plot other columns vs Vin for the subset of the DataFrame
    # Plot other columns vs Vin for the subset of the DataFrame
    if other_cols_groups is not None:
        for other_cols in other_cols_groups:
            plt.figure(figsize=(20, 10))
            min_y = min(subset_df[other_col].min() for other_col in other_cols)
            max_y = max(subset_df[other_col].max() for other_col in other_cols)
            y_range = max_y - min_y
            offset = 0.04  # Adjust this value as needed
            for i, other_col in enumerate(sorted(other_cols, key=lambda col: subset_df[col].min())):
                line, = plt.plot(subset_df[vin_col], subset_df[other_col], marker='o', label=other_col)
                color = line.get_color()

                # Annotate the value of each column at the bounds
                lower_bound_value = '{:.2e}'.format(subset_df.loc[lower_bound, other_col])
                upper_bound_value = '{:.2e}'.format(subset_df.loc[upper_bound, other_col])
                # lower_bound_value = '{:g}'.format(float('{:.3g}'.format(subset_df.loc[lower_bound, other_col])))
                # upper_bound_value = '{:g}'.format(float('{:.3g}'.format(subset_df.loc[upper_bound, other_col])))
                y_coord = min_y + y_range * (i * offset)
                plt.annotate(f'{other_col}={lower_bound_value}', (subset_df.loc[lower_bound, vin_col], y_coord), textcoords="offset points", xytext=(10,-10), ha='left', color=color, fontsize=12)
                plt.annotate(f'{other_col}={upper_bound_value}', (subset_df.loc[upper_bound, vin_col], y_coord), textcoords="offset points", xytext=(10,-10), ha='left', color=color, fontsize=12)

            # Draw vertical lines at the bounds of the linear region
            plt.axvline(x=subset_df.loc[lower_bound, vin_col], color='r', linestyle='--')
            plt.axvline(x=subset_df.loc[upper_bound, vin_col], color='r', linestyle='--')

            plt.title(f'{other_cols} vs Vin')
            plt.xlabel('Vin')
            plt.legend()
            plt.grid(True)
            plt.show()
    return bound_indices
# function to plot arbitrary subplots of column(s) vs column from a pandas DataFrame
def plotdf_subplots(df, cols_groups, subplot_layout, size, marker='o', linestyle='-'):
    fig, axs = plt.subplots(*subplot_layout, figsize=(size[1], size[0]*len(cols_groups)))

    axs = axs.ravel()  # Flatten the array of axes if it's 2D

    for i, (ax, cols) in enumerate(zip(axs, cols_groups)):
        x_col = cols[0]
        y_cols = cols[1:]
        for y_col in y_cols:
            if isinstance(y_col, tuple) and isinstance(y_col[0], pd.Series):
                # Use the Series as the y-data and the second element of the tuple as the label
                y_data = y_col[0]
                label = y_col[1]
            else:
                y_data = df[y_col]
                label = y_col
            ax.plot(df[x_col], y_data, marker=marker, linestyle=linestyle, linewidth=3, label=label)
        ax.set_xlabel(x_col)
        ax.legend()
        ax.grid(True)

    # If there are more subplots than data sets, remove the remaining subplots
    for j in range(i+1, len(axs)):
        fig.delaxes(axs[j])

    plt.tight_layout()
    plt.show()
# function to plot vout(t) and any y(t) vs vin(t) from a pandas DataFrame; returns the indices of the vout vs. vin linear range bounds
def plotdf_dctransfer_from_tran(df, n, vin_col, vout_col, round, other_cols_groups=None, subplot_layout=None):
    # Round Vin to 4 decimal places 
    df['Vin_rounded'] = df[vin_col].round(round)
    # Find the index of the xth occurrence of Vin=0
    zero_indices = np.where(df['Vin_rounded'] == 0)[0]
    
    if len(zero_indices) < n:
        print(f"Not enough occurrences of Vin=0. Only found {len(zero_indices)} occurrences.")
        return

    start = zero_indices[n-1]

    # Find the index where Vin begins to decrease again
    vin_diff = df[vin_col].diff()
    decreasing_indices = np.where(vin_diff[start+1:] < 0)[0]

    if len(decreasing_indices) == 0:
        print("Vin does not begin to decrease after the xth occurrence of Vin=0.")
        return

    end = start + 1 + decreasing_indices[0]

    # Select the subset of the DataFrame between these indices and create a copy
    subset_df = df.iloc[start:end+1].copy()
    # print(subset_df.shape)
    # Compute the derivative of Vout with respect to Vin
    subset_df['Gain'] = subset_df[vout_col].diff() / subset_df[vin_col].diff()
    
    # for i in subset_df['Gain']:
    #     print(i)
    
    # Find the region where the gain is approximately constant
    gain_diff = subset_df['Gain'].diff().abs()
    linear_region = gain_diff < 0.01  # Adjust this threshold as needed
    
    # for i in gain_diff:
    #     print(i)
    
    # Find the bounds that cover the maximum amount of consecutive linear data points
    linear_indices = subset_df[linear_region].index
    # print(linear_indices)
    bounds = [linear_indices[0]]
    # print(bounds)
    for i in range(1, len(linear_indices)):
        if linear_indices[i] - linear_indices[i-1] > 1:
            bounds.append(linear_indices[i])
    bounds.append(linear_indices[-1])
    # print(bounds)

    # Choose the second as the lower bound and the last as the upper bound
    if len(bounds) >= 2:
        lower_bound = bounds[-2]
        upper_bound = bounds[-1]
    else:
        print("Not enough consecutive linear bounds.")
        return
    bound_indices = [lower_bound, upper_bound]
    # print(bound_indices)
    # Create subplots if layout is provided
    if subplot_layout is not None:
        fig, axs = plt.subplots(*subplot_layout, figsize=(32, 4*(len(other_cols_groups)+1)))
        axs = axs.ravel()  # Flatten the array of axes if it's 2D
        ax = axs[0]
    else:
        fig, ax = plt.subplots(figsize=(32, 10))

    # Plot Vout vs Vin for the subset of the DataFrame
    ax.plot(subset_df[vin_col], subset_df[vout_col], marker='o', linewidth=3)

    # Draw vertical lines at the bounds of the linear region
    x1=subset_df.loc[lower_bound, vin_col]
    x2=subset_df.loc[upper_bound, vin_col]
    ax.axvline(x1, color='r', linestyle='--')
    ax.axvline(x2, color='r', linestyle='--')
    # print(x1, x2)

    # Annotate the value of Vin at the bounds
    ax.annotate(f'Vin={subset_df.loc[lower_bound, vin_col]:.3f}', (subset_df.loc[lower_bound, vin_col], subset_df[vout_col].min()), textcoords="offset points", xytext=(10,-10), ha='left', color='red', fontsize=12)
    ax.annotate(f'Vin={subset_df.loc[upper_bound, vin_col]:.3f}', (subset_df.loc[upper_bound, vin_col], subset_df[vout_col].min()), textcoords="offset points", xytext=(10,-10), ha='left', color='red', fontsize=12)
    ax.annotate(f'Vout={subset_df.loc[lower_bound, vout_col]:.3f}', (subset_df.loc[lower_bound, vin_col], subset_df.loc[lower_bound, vout_col]), textcoords="offset points", xytext=(10,-10), ha='left', color='blue', fontsize=12)
    ax.annotate(f'Vout={subset_df.loc[upper_bound, vout_col]:.3f}', (subset_df.loc[upper_bound, vin_col], subset_df.loc[upper_bound,vout_col]), textcoords="offset points", xytext=(10,-10), ha='left', color='blue', fontsize=12)

    ax.set_title('Vout vs Vin')
    ax.set_xlabel('Vin')
    ax.set_ylabel('Vout')
    ax.grid(True)

    # Plot other columns vs Vin for the subset of the DataFrame
    if other_cols_groups is not None:
        for i, other_cols in enumerate(other_cols_groups, start=1 if subplot_layout is not None else 0):
            if subplot_layout is not None:
                ax = axs[i]
            else:
                fig, ax = plt.subplots(figsize=(32, 10))

            min_y = min(subset_df[other_col].min() for other_col in other_cols)
            max_y = max(subset_df[other_col].max() for other_col in other_cols)
            y_range = max_y - min_y
            offset = 0.04  # Adjust this value as needed
            for j, other_col in enumerate(sorted(other_cols, key=lambda col: subset_df[col].min())):  # Changed variable name from i to j
                line, = ax.plot(subset_df[vin_col], subset_df[other_col], marker='o', label=other_col, linewidth=3)
                color = line.get_color()

                # Annotate the value of each column at the bounds
                lower_bound_value = '{:.2e}'.format(subset_df.loc[lower_bound, other_col])
                upper_bound_value = '{:.2e}'.format(subset_df.loc[upper_bound, other_col])
                y_coord = min_y + y_range * (j * offset)  # Changed variable name from i to j
                ax.annotate(f'{other_col}={lower_bound_value}', (subset_df.loc[lower_bound, vin_col], y_coord), textcoords="offset points", xytext=(10,-10), ha='left', color=color, fontsize=14)
                ax.annotate(f'{other_col}={upper_bound_value}', (subset_df.loc[upper_bound, vin_col], y_coord), textcoords="offset points", xytext=(-10,-10), ha='right', color=color, fontsize=14)

            # Draw vertical lines at the bounds of the linear region
            ax.axvline(x=subset_df.loc[lower_bound, vin_col], color='r', linestyle='--')
            ax.axvline(x=subset_df.loc[upper_bound, vin_col], color='r', linestyle='--')

            ax.set_title(f'{other_cols} vs Vin')
            ax.set_xlabel('Vin')
            ax.legend()
            ax.grid(True)

        if subplot_layout is not None:
            # If there are more subplots than data sets, remove the remaining subplots
            for j in range(i+1, len(axs)):
                fig.delaxes(axs[j])
            plt.tight_layout()

    plt.show()

    return bound_indices
# function to plot arbitrary subplots of column(s) vs column from multiple pandas DataFrame
def plotdf_subplots2(df_dict, cols_groups, subplot_layout, size, marker='o', linestyle='-'):
    w = size[0]
    h = size[1]
    fig, axs = plt.subplots(*subplot_layout, figsize=(w, h*len(cols_groups)))

    axs = axs.ravel()  # Flatten the array of axes if it's 2D

    for i, (ax, cols) in enumerate(zip(axs, cols_groups)):
        x_col = cols[0]
        y_cols = cols[1:]

        # Find the maximum of the minimum 'x' values and the minimum of the maximum 'x' values
        x_min = max(df_dict[df_key][x_col].min() for df_key, _ in y_cols)
        x_max = min(df_dict[df_key][x_col].max() for df_key, _ in y_cols)

        for y_col in y_cols:
            df_key, y_col_name = y_col
            # Limit the 'x' and 'y' data to the range [x_min, x_max]
            mask = (df_dict[df_key][x_col] >= x_min) & (df_dict[df_key][x_col] <= x_max)
            x_data = df_dict[df_key][x_col][mask]
            y_data = df_dict[df_key][y_col_name][mask]
            ax.plot(x_data, y_data, marker=marker, linestyle=linestyle, label=y_col_name)
        ax.set_xlabel(x_col)
        ax.legend()
        ax.grid(True)

    # If there are more subplots than data sets, remove the remaining subplots
    for j in range(i+1, len(axs)):
        fig.delaxes(axs[j])

    plt.tight_layout()
    plt.show()
# function to group the columns of a pandas DataFrame by the period of a column
def group_by_period(df, colx, coly):
    # Compute the autocorrelation of the chosen column
    autocorr = np.correlate(df[coly], df[coly], mode='full')

    # Compute the derivative of the autocorrelation
    derivative = np.diff(autocorr)

    # Identify the indices where the derivative changes from positive to negative
    # maxima_indices = np.where(np.diff(np.sign(derivative)) == -2)[0] + 1
    maxima_indices = np.where(np.diff(np.sign(derivative)) != 0)[0] + 1
    
    # Create a new column 'period' that assigns a period number to each row
    df['period'] = np.searchsorted(maxima_indices, df.index, side='right')

    # Adjust the 'period' column to group by periods from one local maxima to the next
    df['period'] = df['period'] % len(maxima_indices)

    # Create a dictionary of dataframes, each representing a period
    dfs_period = {period: group for period, group in df.groupby('period')}

    # Create a figure with subplots for each maxima index plus one for the original series
    fig, axs = plt.subplots(len(maxima_indices) + 1, 1, sharex=True, figsize=(10, 6 * (len(maxima_indices) + 1)))

    # Plot coly vs colx in the first subplot
    axs[0].plot(df[colx], df[coly])
    axs[0].set_title('Original')
    axs[0].grid(True)

    # Plot coly from the i'th local maxima to the i+1'th local maxima vs colx in the remaining subplots
    for i in range(len(maxima_indices) - 1):
        start, end = maxima_indices[i], maxima_indices[i + 1]
        shifted_coly = df[coly].copy()
        shifted_coly[:start] = 0
        shifted_coly[end:] = 0
        axs[i + 1].plot(df[colx], shifted_coly)
        axs[i + 1].set_title(f'From maxima {i} to {i + 1}')
        axs[i + 1].grid(True)

    fig.suptitle(coly + ' versus ' + colx)
    plt.xlabel(colx)
    plt.show()

    # Plot the autocorrelation
    plt.figure(figsize=(10, 6))
    plt.plot(autocorr)
    plt.title('Autocorrelation of ' + coly)
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.grid(True)
    plt.show()

    return dfs_period, maxima_indices

def group_by_hperiod(df, colx, coly):
    # Compute the autocorrelation of the chosen column
    autocorr = np.correlate(df[coly], df[coly], mode='full')

    # Compute the derivative of the autocorrelation
    derivative = np.diff(autocorr)

    # Identify the indices where the derivative changes sign
    extrema_indices = np.where(np.diff(np.sign(derivative)) != 0)[0] + 1

    # Create a new column 'period' that assigns a period number to each row
    df['period'] = np.searchsorted(extrema_indices, df.index, side='right')

    # Create a dictionary of dataframes, each representing a period
    dfs_period = {period: group for period, group in df.groupby('period')}

    # Plot coly vs colx
    plt.figure(figsize=(10, 6))
    plt.plot(df[colx], df[coly], label='Original')

    # Overlay plots of coly shifted by the extrema indices vs colx
    for shift in extrema_indices:
        shifted_coly = np.roll(df[coly], shift)  # Shift coly by the current extrema index
        plt.plot(df[colx], shifted_coly, label=f'Shifted by {shift}')

    plt.title(coly + ' versus ' + colx)
    plt.xlabel(colx)
    plt.ylabel(coly)
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot the autocorrelation
    plt.figure(figsize=(10, 6))
    plt.plot(autocorr)
    plt.title('Autocorrelation of ' + coly)
    plt.xlabel('Lag')
    plt.ylabel('Autocorrelation')
    plt.grid(True)
    plt.show()

    return dfs_period, extrema_indices

def subset_df_by_derivative(df, colx, coly):
    # Compute the derivative of coly with respect to colx
    df['derivative'] = df[coly].diff() / df[colx].diff()

    # Identify the indices where the derivative changes from negative to positive
    rising_indices = np.where(np.diff(np.sign(df['derivative'])) == 2)[0]

    # Identify the indices where the derivative changes from positive to negative
    falling_indices = np.where(np.diff(np.sign(df['derivative'])) == -2)[0]

    # Find the first rising index and the first falling index that comes after it
    for start in rising_indices:
        end = falling_indices[falling_indices > start]
        if end.size > 0:
            # Create a subset of the DataFrame that includes only the rows from when the derivative changes from negative to positive to the next time the derivative changes from positive to negative
            subset_df = df.iloc[start:end[0]]
            return subset_df

    # If no such range is found, return an empty DataFrame
    return pd.DataFrame(columns=df.columns)