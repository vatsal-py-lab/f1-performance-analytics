{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOW5D8q1OlLuAh4Frm10Lxy",
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
      "execution_count": 410,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "K402xPm9czfI",
        "outputId": "a260cade-79e8-435a-bddd-5803e1c8fbfd",
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
      "execution_count": 411,
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
        "outputId": "29b74537-b243-47be-de92-cebd1b2498ad"
      },
      "execution_count": 412,
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
      "execution_count": 413,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# print columns using 'get_event_schedule' function for year 2025\n",
        "schedule = fastf1.get_event_schedule(2025)\n",
        "print(schedule.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pXiKnZCjGAWF",
        "outputId": "3dfea344-73f6-4327-b712-72bb4de05ae7"
      },
      "execution_count": 414,
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
      "execution_count": 415,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# print columns using 'get_event_schedule' function for year 2025\n",
        "\n",
        "session = fastf1.get_session(2025, 'Melbourne', 'R')\n",
        "session.load()\n",
        "print(session.laps.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "RSX7VHtGSnHJ",
        "outputId": "e8c58883-9241-4f09-e722-4e63fff9a20b"
      },
      "execution_count": 416,
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
        "driver = pd.DataFrame(columns=['DriverId', 'DriverCode', 'Team', 'CarNumber'])\n",
        "driverName = {d: session.get_driver(d)['FullName'] for d in session.laps['Driver'].unique()}\n",
        "driverName = pd.DataFrame(list(driverName.items()), columns=['DriverCode', 'DriverName'])\n",
        "driver['Team'] = session.laps['Team']\n",
        "driver['DriverCode'] = session.laps['Driver']\n",
        "driver['CarNumber'] = session.laps['DriverNumber']\n",
        "driver = driver.drop_duplicates().sort_values(by=['Team'])\n",
        "driver['DriverId'] = range(1, len(session.laps['Driver'].unique()) + 1)\n",
        "drivers = pd.merge(driver, driverName, on=\"DriverCode\", how=\"left\")\n",
        "print(drivers[['DriverId', 'DriverCode', 'DriverName', 'Team', 'CarNumber']])\n",
        "drivers.to_csv('drivers.csv', index=False)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-BXLHD2NU5IA",
        "outputId": "801a7703-35d5-4552-aef7-d113f7bf2bc2"
      },
      "execution_count": 417,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "    DriverId DriverCode             DriverName             Team CarNumber\n",
            "0          1        GAS           Pierre Gasly           Alpine        10\n",
            "1          2        DOO            Jack Doohan           Alpine         7\n",
            "2          3        ALO        Fernando Alonso     Aston Martin        14\n",
            "3          4        STR           Lance Stroll     Aston Martin        18\n",
            "4          5        LEC        Charles Leclerc          Ferrari        16\n",
            "5          6        HAM         Lewis Hamilton          Ferrari        44\n",
            "6          7        BEA         Oliver Bearman     Haas F1 Team        87\n",
            "7          8        OCO           Esteban Ocon     Haas F1 Team        31\n",
            "8          9        HUL        Nico Hulkenberg      Kick Sauber        27\n",
            "9         10        BOR      Gabriel Bortoleto      Kick Sauber         5\n",
            "10        11        PIA          Oscar Piastri          McLaren        81\n",
            "11        12        NOR           Lando Norris          McLaren         4\n",
            "12        13        ANT  Andrea Kimi Antonelli         Mercedes        12\n",
            "13        14        RUS         George Russell         Mercedes        63\n",
            "14        15        TSU           Yuki Tsunoda     Racing Bulls        22\n",
            "15        16        HAD           Isack Hadjar     Racing Bulls         6\n",
            "16        17        VER         Max Verstappen  Red Bull Racing         1\n",
            "17        18        LAW            Liam Lawson  Red Bull Racing        30\n",
            "18        19        ALB        Alexander Albon         Williams        23\n",
            "19        20        SAI           Carlos Sainz         Williams        55\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# creating data tables - laps\n",
        "\n",
        "print(session.laps.columns)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bpzxxqk-v5Hn",
        "outputId": "874d5526-c890-4d51-e85f-ba4935e6da3b"
      },
      "execution_count": 418,
      "outputs": [
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
        "laps = session.laps[['Driver', 'DriverNumber', 'LapNumber', 'LapTime', 'Sector1Time', 'Sector2Time', 'Sector3Time',\n",
        "                     'Position', 'Stint', 'Compound', 'TyreLife', 'PitInTime', 'PitOutTime', 'TrackStatus']]\n",
        "laps.insert(0, 'LapId', range(1, len(laps) + 1))\n",
        "\n",
        "laps = pd.merge(laps, drivers[['DriverId', 'DriverCode']], left_on='Driver', right_on='DriverCode', how='left')\n",
        "laps = laps.drop(columns=['DriverCode'])\n",
        "laps = laps[['DriverId', 'Driver', 'LapId', 'LapNumber', 'LapTime', 'LapTime', 'Sector1Time', 'Sector2Time', 'Sector3Time',\n",
        "                     'Position', 'Stint', 'Compound', 'TyreLife', 'PitInTime', 'PitOutTime', 'TrackStatus']]\n",
        "laps.to_csv('laps.csv', index=False)"
      ],
      "metadata": {
        "id": "pRxmQJW0_0r-"
      },
      "execution_count": 419,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "HYTVrLyg5PBG"
      },
      "execution_count": 419,
      "outputs": []
    }
  ]
}