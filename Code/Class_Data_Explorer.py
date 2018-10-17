import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from Code.Class_Data_Loader import DataLoader


class DataExploration(DataLoader):
    def __init__(self, data_set):
        super().__init__(data_set)

    # method that returns the number of different values in a given column
    def column_value_count(self, attribute):
        #  first counts the number of different values in each column then sorts it in ascending order
        column_count = self._data_set[attribute].value_counts().sort_index()
        print("The count of the different variables in the attribute: ", attribute, ' is\n', column_count)

    # method that prints a summary of the distribution of the data
    def describe_attribute(self, attribute):
        description_of_attribute = self._data_set[attribute].describe()
        print("A summary of the disribution for the attribute", attribute, ' is\n', description_of_attribute)

    #  method that prints the percentage of missing data of each column
    def missing_data_ratio_print(self):
        #  define the percentage as the number of missing values in each column/ number of entries * 100
        percent_of_missing_data_in_each_column = ((self._data_set.isnull().sum() / (len(self._data_set))) * 100)

        #  sorts percent_of_missing_data_in_each_column into descending order to be printed
        percent_of_missing_data_in_each_column = percent_of_missing_data_in_each_column.drop(
            percent_of_missing_data_in_each_column[percent_of_missing_data_in_each_column == 0].index).sort_values(
            ascending=False)[:self._data_set.shape[1]]

        #  redefines percent_of_missing_data_in_each_column as a DataFrame with the column head 'Missing Ratio'
        percent_of_missing_data_in_each_column = pd.DataFrame({'Missing Ratio': percent_of_missing_data_in_each_column})
        #  rename the column heading
        percent_of_missing_data_in_each_column = percent_of_missing_data_in_each_column.rename(columns={
            percent_of_missing_data_in_each_column.columns[0]: "Percentage of missing values"})

        #  print the data fame
        print(percent_of_missing_data_in_each_column.head(20))

    #  method that p
    def missing_data_ratio_bar_graph(self):
        #  define the percentage as the number of missing values in each column/ number of entries * 100
        percent_of_missing_data_in_each_column = ((self._data_set.isnull().sum() / (len(self._data_set))) * 100)

        #  sorts percent_of_missing_data_in_each_column into descending order to be printed
        percent_of_missing_data_in_each_column = percent_of_missing_data_in_each_column.drop(
            percent_of_missing_data_in_each_column[percent_of_missing_data_in_each_column == 0].index).sort_values(
                ascending=False)[:self._data_set.shape[1]]

        plt.xticks(rotation='90', fontsize=14)
        # use seaborn package to plot the bar graph
        sns.barplot(x=percent_of_missing_data_in_each_column.index, y=percent_of_missing_data_in_each_column)
        plt.xlabel('Attribute', fontsize=15)
        plt.ylabel('Percent of missing values', fontsize=15)
        plt.title('Percent missing data by feature', fontsize=15)
        plt.savefig('Data_Out/percentage_of_missing_data.pdf', index=False, bbox_inches='tight')  # save the plot
        plt.show()

    # method that creates a bar graph to show the distribution of an attribute
    def bar_graph_distribution(self, attribute):
        #  first counts the number of different values in each column then sorts it in ascending order
        column_count = self._data_set[attribute].value_counts().sort_index()

        # set the y axis to the values within the series object as a percentage
        y = column_count.values * 100 / column_count.sum()
        x = column_count.index  # set the x axis to the index of the series object
        width_of_bar = 1 / 1.5
        plt.subplots(figsize=(16, 8))  # changes the size of the fig

        plt.bar(x, y, width_of_bar, color="#2b8cbe", edgecolor='black', linewidth=2)  # plots the bar graph
        #  plt.title('Bar graph of ' + str(column_count.name) + ' Against ' + str(' Sample Size'), fontsize=20)
        plt.xlabel(column_count.name, fontsize=15)  # sets the xlabel to the name of the series object
        plt.ylabel('Percent', fontsize=15)
        plt.xticks(x, rotation=90)  # rotates ticks by 90deg so larger font can be used
        plt.tick_params(labelsize=12)  # increases font of the ticks

        #  file name defined by attribute user input and type of graph
        plt.savefig('Data_Out/' + attribute + '_bar_graph_percentage.pdf', index=False, bbox_inches='tight')
        plt.show()
