import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city
    while True:
        city = input("Enter the city (chicago, new york city, washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please enter a valid city name (chicago, new york city, washington):")
    
    # Get user input for month
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input("Enter the month (all, january, february, ..., june): ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month (all, january, february, ..., june): ")
    
    # Get user input for day of week
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        day = input("Enter the day (all, monday, tuesday, ..., sunday): ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day (all, monday, tuesday, ..., sunday): ")
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    # 1st to Convert the Start Time column to datetime then to extract the month and day of week from Start Time to create new columns
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour
    
    # Filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month]
    
    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day'] == day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['month'].mode()[0]
    print('The Most Common Month:', common_month)

    # Display the most common day of week
    common_day = df['day'].mode()[0]
    print('The Most Common Day of Week:', common_day)

    # Display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('The Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)

    # Display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)

    # Display most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('Most Frequent Combination of Start Station and End Station:', common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    # Display the most common trip duration
    common_trip_duration = df['Trip Duration'].mode()[0]
    print('Most Common Trip Duration:', common_trip_duration)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Gender Counts:\n', gender_counts)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('Earliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw_data(df):
    """Displays raw data in chunks of 5 rows based on user input."""
    row_index = 0
    total_rows = len(df)

    while row_index < total_rows:
        user_input = input("Would you like to see 5 lines of raw data? Choose either 'yes' or 'no'? ").strip().lower()
        if user_input == 'yes':
            print(df.iloc[row_index:row_index + 5])
            row_index += 5
        elif user_input == 'no':
            print("No more data will be displayed.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if row_index >= total_rows:
        print("All data has been displayed.")
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()

