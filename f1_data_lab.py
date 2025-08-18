{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPKKbaJFBgUcaMga2/7liYq",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vatsal-py-lab/f1-data-lab/blob/main/f1_data_lab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K402xPm9czfI",
        "outputId": "33b73aaf-761c-49d7-f64c-b75b948ea98d",
        "collapsed": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: fastf1 in /usr/local/lib/python3.11/dist-packages (3.6.0)\n",
            "Requirement already satisfied: matplotlib<4.0.0,>=3.5.1 in /usr/local/lib/python3.11/dist-packages (from fastf1) (3.10.0)\n",
            "Requirement already satisfied: numpy<3.0.0,>=1.23.1 in /usr/local/lib/python3.11/dist-packages (from fastf1) (2.0.2)\n",
            "Requirement already satisfied: pandas<3.0.0,>=1.4.1 in /usr/local/lib/python3.11/dist-packages (from fastf1) (2.2.2)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.11/dist-packages (from fastf1) (2.9.0.post0)\n",
            "Requirement already satisfied: rapidfuzz in /usr/local/lib/python3.11/dist-packages (from fastf1) (3.13.0)\n",
            "Requirement already satisfied: requests-cache>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from fastf1) (1.2.1)\n",
            "Requirement already satisfied: requests>=2.28.1 in /usr/local/lib/python3.11/dist-packages (from fastf1) (2.32.3)\n",
            "Requirement already satisfied: scipy<2.0.0,>=1.8.1 in /usr/local/lib/python3.11/dist-packages (from fastf1) (1.16.1)\n",
            "Requirement already satisfied: timple>=0.1.6 in /usr/local/lib/python3.11/dist-packages (from fastf1) (0.1.8)\n",
            "Requirement already satisfied: websockets<14,>=10.3 in /usr/local/lib/python3.11/dist-packages (from fastf1) (13.1)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (1.3.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.11/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.11/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (4.59.0)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (1.4.9)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.11/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (25.0)\n",
            "Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.11/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (11.3.0)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.11/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (3.2.3)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3.0.0,>=1.4.1->fastf1) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3.0.0,>=1.4.1->fastf1) (2025.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil->fastf1) (1.17.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests>=2.28.1->fastf1) (3.4.3)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests>=2.28.1->fastf1) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests>=2.28.1->fastf1) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests>=2.28.1->fastf1) (2025.8.3)\n",
            "Requirement already satisfied: attrs>=21.2 in /usr/local/lib/python3.11/dist-packages (from requests-cache>=1.0.0->fastf1) (25.3.0)\n",
            "Requirement already satisfied: cattrs>=22.2 in /usr/local/lib/python3.11/dist-packages (from requests-cache>=1.0.0->fastf1) (25.1.1)\n",
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests-cache>=1.0.0->fastf1) (4.3.8)\n",
            "Requirement already satisfied: url-normalize>=1.4 in /usr/local/lib/python3.11/dist-packages (from requests-cache>=1.0.0->fastf1) (2.2.1)\n",
            "Requirement already satisfied: typing-extensions>=4.12.2 in /usr/local/lib/python3.11/dist-packages (from cattrs>=22.2->requests-cache>=1.0.0->fastf1) (4.14.1)\n"
          ]
        }
      ],
      "source": [
        "#install fastf1 library\n",
        "\n",
        "!pip install fastf1"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# import libraries\n",
        "\n",
        "import pkgutil\n",
        "import fastf1\n",
        "import pandas as pd\n",
        "import os"
      ],
      "metadata": {
        "id": "fzoBVTwI_H-x"
      },
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# list modules programmatically\n",
        "\n",
        "modules = [m.name for m in pkgutil.iter_modules(fastf1.__path__)]\n",
        "print(modules)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "adA9AezsFhsk",
        "outputId": "e7b42c28-9bc9-42ab-b54e-41d663ce8e70"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['_api', '_version', 'api', 'core', 'ergast', 'events', 'internals', 'legacy', 'livetiming', 'logger', 'mvapi', 'plotting', 'req', 'signalr_aio', 'utils']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# sets up a cache directory\n",
        "cache_dir = 'cache'\n",
        "if not os.path.exists(cache_dir):\n",
        "    os.makedirs(cache_dir)\n",
        "\n",
        "# enables the fastf1 cache\n",
        "fastf1.Cache.enable_cache(cache_dir)"
      ],
      "metadata": {
        "id": "tjprtWKOF9ux"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# print columns using 'get_event_schedule' function for year 2025\n",
        "season = 2025\n",
        "schedule = fastf1.get_event_schedule(season)\n",
        "print(schedule.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pXiKnZCjGAWF",
        "outputId": "c0762276-371d-4e5d-8976-b02bcd4e98a2"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['RoundNumber', 'Country', 'Location', 'OfficialEventName', 'EventDate',\n",
            "       'EventName', 'EventFormat', 'Session1', 'Session1Date',\n",
            "       'Session1DateUtc', 'Session2', 'Session2Date', 'Session2DateUtc',\n",
            "       'Session3', 'Session3Date', 'Session3DateUtc', 'Session4',\n",
            "       'Session4Date', 'Session4DateUtc', 'Session5', 'Session5Date',\n",
            "       'Session5DateUtc', 'F1ApiSupport'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# creating data tables - events\n",
        "\n",
        "today = pd.Timestamp.today().normalize()\n",
        "schedule['Completed'] = schedule['EventDate'] < today\n",
        "schedule['EventID'] = schedule['RoundNumber'] + 1\n",
        "schedule['Year'] = \"2025\"\n",
        "events = schedule[['EventID', 'Year', 'EventName', 'Country', 'Location', 'EventDate', 'EventFormat', 'Completed']]\n",
        "events.to_csv('events.csv', index=False)"
      ],
      "metadata": {
        "id": "_yKQqEJYFZyk"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# print columns using 'get_session' function for Melbourne GP for year 2025\n",
        "\n",
        "location = 'Melbourne'\n",
        "session_type = 'R'\n",
        "session = fastf1.get_session(season, location, session_type)\n",
        "session.load()\n",
        "print(session.laps.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RSX7VHtGSnHJ",
        "outputId": "d6cc06d5-d60d-403e-bf31-6a1dabd5acfe"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "core           INFO \tLoading data for Australian Grand Prix - Race [v3.6.0]\n",
            "INFO:fastf1.fastf1.core:Loading data for Australian Grand Prix - Race [v3.6.0]\n",
            "req            INFO \tUsing cached data for session_info\n",
            "INFO:fastf1.fastf1.req:Using cached data for session_info\n",
            "req            INFO \tUsing cached data for driver_info\n",
            "INFO:fastf1.fastf1.req:Using cached data for driver_info\n",
            "req            INFO \tUsing cached data for session_status_data\n",
            "INFO:fastf1.fastf1.req:Using cached data for session_status_data\n",
            "req            INFO \tUsing cached data for lap_count\n",
            "INFO:fastf1.fastf1.req:Using cached data for lap_count\n",
            "req            INFO \tUsing cached data for track_status_data\n",
            "INFO:fastf1.fastf1.req:Using cached data for track_status_data\n",
            "req            INFO \tUsing cached data for _extended_timing_data\n",
            "INFO:fastf1.fastf1.req:Using cached data for _extended_timing_data\n",
            "req            INFO \tUsing cached data for timing_app_data\n",
            "INFO:fastf1.fastf1.req:Using cached data for timing_app_data\n",
            "core           INFO \tProcessing timing data...\n",
            "INFO:fastf1.fastf1.core:Processing timing data...\n",
            "core        WARNING \tFixed incorrect tyre stint information for driver '87'\n",
            "WARNING:fastf1.fastf1.core:Fixed incorrect tyre stint information for driver '87'\n",
            "core        WARNING \tFixed incorrect tyre stint information for driver '30'\n",
            "WARNING:fastf1.fastf1.core:Fixed incorrect tyre stint information for driver '30'\n",
            "core        WARNING \tFixed incorrect tyre stint information for driver '5'\n",
            "WARNING:fastf1.fastf1.core:Fixed incorrect tyre stint information for driver '5'\n",
            "req            INFO \tUsing cached data for car_data\n",
            "INFO:fastf1.fastf1.req:Using cached data for car_data\n",
            "req            INFO \tUsing cached data for position_data\n",
            "INFO:fastf1.fastf1.req:Using cached data for position_data\n",
            "req            INFO \tUsing cached data for weather_data\n",
            "INFO:fastf1.fastf1.req:Using cached data for weather_data\n",
            "req            INFO \tUsing cached data for race_control_messages\n",
            "INFO:fastf1.fastf1.req:Using cached data for race_control_messages\n",
            "core        WARNING \tDriver 4 completed the race distance 00:00.022000 before the recorded end of the session.\n",
            "WARNING:fastf1.fastf1.core:Driver 4 completed the race distance 00:00.022000 before the recorded end of the session.\n",
            "core           INFO \tFinished loading data for 20 drivers: ['4', '1', '63', '12', '23', '18', '27', '16', '81', '44', '10', '22', '31', '87', '30', '5', '14', '55', '7', '6']\n",
            "INFO:fastf1.fastf1.core:Finished loading data for 20 drivers: ['4', '1', '63', '12', '23', '18', '27', '16', '81', '44', '10', '22', '31', '87', '30', '5', '14', '55', '7', '6']\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Index(['Time', 'Driver', 'DriverNumber', 'LapTime', 'LapNumber', 'Stint',\n",
            "       'PitOutTime', 'PitInTime', 'Sector1Time', 'Sector2Time', 'Sector3Time',\n",
            "       'Sector1SessionTime', 'Sector2SessionTime', 'Sector3SessionTime',\n",
            "       'SpeedI1', 'SpeedI2', 'SpeedFL', 'SpeedST', 'IsPersonalBest',\n",
            "       'Compound', 'TyreLife', 'FreshTyre', 'Team', 'LapStartTime',\n",
            "       'LapStartDate', 'TrackStatus', 'Position', 'Deleted', 'DeletedReason',\n",
            "       'FastF1Generated', 'IsAccurate'],\n",
            "      dtype='object')\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# creating data tables - drivers\n",
        "\n",
        "driver = session.results[['Abbreviation', 'FullName', 'TeamName', 'DriverNumber']].copy()\n",
        "driver.rename(columns={'Abbreviation': 'DriverCode',\n",
        "                       'FullName': 'DriverName',\n",
        "                       'TeamName': 'Team',\n",
        "                       'DriverNumber': 'CarNumber'}, inplace=True)\n",
        "driver['DriverId'] = range(1, len(driver) + 1)\n",
        "driver = driver[['DriverId', 'DriverCode', 'DriverName', 'Team', 'CarNumber']]\n",
        "driver.to_csv('drivers.csv', index=False)"
      ],
      "metadata": {
        "id": "calF8CLpduq1"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# creating data tables - laps\n",
        "\n",
        "laps = session.laps[['Driver', 'DriverNumber', 'LapNumber', 'LapTime', 'Sector1Time', 'Sector2Time', 'Sector3Time',\n",
        "                     'Position', 'Stint', 'Compound', 'TyreLife', 'PitInTime', 'PitOutTime', 'TrackStatus']]\n",
        "laps.insert(0, 'LapId', range(1, len(laps) + 1))\n",
        "laps = pd.merge(laps, driver[['DriverId', 'DriverCode']], left_on='Driver', right_on='DriverCode', how='left')\n",
        "laps = laps.drop(columns=['DriverCode'])\n",
        "laps = laps[['DriverId', 'Driver', 'LapId', 'LapNumber', 'LapTime', 'LapTime', 'Sector1Time', 'Sector2Time', 'Sector3Time',\n",
        "                     'Position', 'Stint', 'Compound', 'TyreLife', 'PitInTime', 'PitOutTime', 'TrackStatus']]\n",
        "laps.to_csv('laps.csv', index=False)"
      ],
      "metadata": {
        "id": "pRxmQJW0_0r-"
      },
      "execution_count": 9,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# creating data tables - weather\n",
        "\n",
        "weather = session.weather_data\n",
        "weather.insert(0, 'WeatherId', range(1, len(weather) + 1))\n",
        "weather[\"Session\"] = session_type\n",
        "weather = weather[['WeatherId', 'Session', 'Time', 'AirTemp', 'Humidity', 'Pressure', 'Rainfall', 'TrackTemp', 'WindDirection', 'WindSpeed']]\n",
        "weather.to_csv('weather.csv', index=False)"
      ],
      "metadata": {
        "id": "HYTVrLyg5PBG"
      },
      "execution_count": 10,
      "outputs": []
    }
  ]
}