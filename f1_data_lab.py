{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN1hsSBTnv7bc2rsuT58U0X",
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
        "<a href=\"https://colab.research.google.com/github/vatsal-py-lab/f1-performance-analytics/blob/main/f1_data_lab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
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
        "outputId": "31ccf0db-0e7f-4d66-d63f-f318fd9694af",
        "collapsed": true
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting fastf1\n",
            "  Downloading fastf1-3.6.0-py3-none-any.whl.metadata (4.6 kB)\n",
            "Requirement already satisfied: matplotlib<4.0.0,>=3.5.1 in /usr/local/lib/python3.12/dist-packages (from fastf1) (3.10.0)\n",
            "Requirement already satisfied: numpy<3.0.0,>=1.23.1 in /usr/local/lib/python3.12/dist-packages (from fastf1) (2.0.2)\n",
            "Requirement already satisfied: pandas<3.0.0,>=1.4.1 in /usr/local/lib/python3.12/dist-packages (from fastf1) (2.2.2)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.12/dist-packages (from fastf1) (2.9.0.post0)\n",
            "Collecting rapidfuzz (from fastf1)\n",
            "  Downloading rapidfuzz-3.13.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (12 kB)\n",
            "Collecting requests-cache>=1.0.0 (from fastf1)\n",
            "  Downloading requests_cache-1.2.1-py3-none-any.whl.metadata (9.9 kB)\n",
            "Requirement already satisfied: requests>=2.28.1 in /usr/local/lib/python3.12/dist-packages (from fastf1) (2.32.4)\n",
            "Requirement already satisfied: scipy<2.0.0,>=1.8.1 in /usr/local/lib/python3.12/dist-packages (from fastf1) (1.16.1)\n",
            "Collecting timple>=0.1.6 (from fastf1)\n",
            "  Downloading timple-0.1.8-py3-none-any.whl.metadata (2.0 kB)\n",
            "Collecting websockets<14,>=10.3 (from fastf1)\n",
            "  Downloading websockets-13.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.8 kB)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (1.3.3)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.12/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (0.12.1)\n",
            "Requirement already satisfied: fonttools>=4.22.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (4.59.1)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (1.4.9)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (25.0)\n",
            "Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.12/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (11.3.0)\n",
            "Requirement already satisfied: pyparsing>=2.3.1 in /usr/local/lib/python3.12/dist-packages (from matplotlib<4.0.0,>=3.5.1->fastf1) (3.2.3)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.12/dist-packages (from pandas<3.0.0,>=1.4.1->fastf1) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.12/dist-packages (from pandas<3.0.0,>=1.4.1->fastf1) (2025.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.12/dist-packages (from python-dateutil->fastf1) (1.17.0)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests>=2.28.1->fastf1) (3.4.3)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests>=2.28.1->fastf1) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests>=2.28.1->fastf1) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests>=2.28.1->fastf1) (2025.8.3)\n",
            "Requirement already satisfied: attrs>=21.2 in /usr/local/lib/python3.12/dist-packages (from requests-cache>=1.0.0->fastf1) (25.3.0)\n",
            "Collecting cattrs>=22.2 (from requests-cache>=1.0.0->fastf1)\n",
            "  Downloading cattrs-25.1.1-py3-none-any.whl.metadata (8.4 kB)\n",
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests-cache>=1.0.0->fastf1) (4.3.8)\n",
            "Collecting url-normalize>=1.4 (from requests-cache>=1.0.0->fastf1)\n",
            "  Downloading url_normalize-2.2.1-py3-none-any.whl.metadata (5.6 kB)\n",
            "Requirement already satisfied: typing-extensions>=4.12.2 in /usr/local/lib/python3.12/dist-packages (from cattrs>=22.2->requests-cache>=1.0.0->fastf1) (4.14.1)\n",
            "Downloading fastf1-3.6.0-py3-none-any.whl (148 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m148.4/148.4 kB\u001b[0m \u001b[31m8.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading requests_cache-1.2.1-py3-none-any.whl (61 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m61.4/61.4 kB\u001b[0m \u001b[31m5.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading timple-0.1.8-py3-none-any.whl (17 kB)\n",
            "Downloading websockets-13.1-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (165 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m165.0/165.0 kB\u001b[0m \u001b[31m15.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading rapidfuzz-3.13.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m3.1/3.1 MB\u001b[0m \u001b[31m75.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading cattrs-25.1.1-py3-none-any.whl (69 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m69.4/69.4 kB\u001b[0m \u001b[31m6.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading url_normalize-2.2.1-py3-none-any.whl (14 kB)\n",
            "Installing collected packages: websockets, url-normalize, rapidfuzz, cattrs, requests-cache, timple, fastf1\n",
            "  Attempting uninstall: websockets\n",
            "    Found existing installation: websockets 15.0.1\n",
            "    Uninstalling websockets-15.0.1:\n",
            "      Successfully uninstalled websockets-15.0.1\n",
            "\u001b[31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
            "google-adk 1.11.0 requires websockets<16.0.0,>=15.0.1, but you have websockets 13.1 which is incompatible.\n",
            "dataproc-spark-connect 0.8.3 requires websockets>=14.0, but you have websockets 13.1 which is incompatible.\u001b[0m\u001b[31m\n",
            "\u001b[0mSuccessfully installed cattrs-25.1.1 fastf1-3.6.0 rapidfuzz-3.13.0 requests-cache-1.2.1 timple-0.1.8 url-normalize-2.2.1 websockets-13.1\n"
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
        "outputId": "45a790c3-3fed-4779-94ef-273b157ccd98"
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
        "outputId": "3c21d2cb-58f9-4581-ef86-760a0d995f51"
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
        "outputId": "4c930a1f-a0a1-4ad6-b85b-6643f67ae7bb"
      },
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "core           INFO \tLoading data for Australian Grand Prix - Race [v3.6.0]\n",
            "INFO:fastf1.fastf1.core:Loading data for Australian Grand Prix - Race [v3.6.0]\n",
            "req            INFO \tNo cached data found for session_info. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for session_info. Loading data...\n",
            "_api           INFO \tFetching session info data...\n",
            "INFO:fastf1.api:Fetching session info data...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for driver_info. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for driver_info. Loading data...\n",
            "_api           INFO \tFetching driver list...\n",
            "INFO:fastf1.api:Fetching driver list...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for session_status_data. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for session_status_data. Loading data...\n",
            "_api           INFO \tFetching session status data...\n",
            "INFO:fastf1.api:Fetching session status data...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for lap_count. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for lap_count. Loading data...\n",
            "_api           INFO \tFetching lap count data...\n",
            "INFO:fastf1.api:Fetching lap count data...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for track_status_data. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for track_status_data. Loading data...\n",
            "_api           INFO \tFetching track status data...\n",
            "INFO:fastf1.api:Fetching track status data...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for _extended_timing_data. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for _extended_timing_data. Loading data...\n",
            "_api           INFO \tFetching timing data...\n",
            "INFO:fastf1.api:Fetching timing data...\n",
            "_api           INFO \tParsing timing data...\n",
            "INFO:fastf1.api:Parsing timing data...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for timing_app_data. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for timing_app_data. Loading data...\n",
            "_api           INFO \tFetching timing app data...\n",
            "INFO:fastf1.api:Fetching timing app data...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "core           INFO \tProcessing timing data...\n",
            "INFO:fastf1.fastf1.core:Processing timing data...\n",
            "core        WARNING \tFixed incorrect tyre stint information for driver '87'\n",
            "WARNING:fastf1.fastf1.core:Fixed incorrect tyre stint information for driver '87'\n",
            "core        WARNING \tFixed incorrect tyre stint information for driver '30'\n",
            "WARNING:fastf1.fastf1.core:Fixed incorrect tyre stint information for driver '30'\n",
            "core        WARNING \tFixed incorrect tyre stint information for driver '5'\n",
            "WARNING:fastf1.fastf1.core:Fixed incorrect tyre stint information for driver '5'\n",
            "req            INFO \tNo cached data found for car_data. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for car_data. Loading data...\n",
            "_api           INFO \tFetching car data...\n",
            "INFO:fastf1.api:Fetching car data...\n",
            "_api           INFO \tParsing car data...\n",
            "INFO:fastf1.api:Parsing car data...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for position_data. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for position_data. Loading data...\n",
            "_api           INFO \tFetching position data...\n",
            "INFO:fastf1.api:Fetching position data...\n",
            "_api           INFO \tParsing position data...\n",
            "INFO:fastf1.api:Parsing position data...\n",
            "_api        WARNING \tDriver 241: Position data is incomplete!\n",
            "WARNING:fastf1.api:Driver 241: Position data is incomplete!\n",
            "_api        WARNING \tDriver 242: Position data is incomplete!\n",
            "WARNING:fastf1.api:Driver 242: Position data is incomplete!\n",
            "_api        WARNING \tDriver 243: Position data is incomplete!\n",
            "WARNING:fastf1.api:Driver 243: Position data is incomplete!\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for weather_data. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for weather_data. Loading data...\n",
            "_api           INFO \tFetching weather data...\n",
            "INFO:fastf1.api:Fetching weather data...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
            "req            INFO \tNo cached data found for race_control_messages. Loading data...\n",
            "INFO:fastf1.fastf1.req:No cached data found for race_control_messages. Loading data...\n",
            "_api           INFO \tFetching race control messages...\n",
            "INFO:fastf1.api:Fetching race control messages...\n",
            "req            INFO \tData has been written to cache!\n",
            "INFO:fastf1.fastf1.req:Data has been written to cache!\n",
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
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "hk62KqMtWFq7"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}