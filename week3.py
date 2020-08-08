#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails


def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])

def get_year(car):
  return"{}".format(car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8') #For Linux
  #locale.setlocale(locale.LC_ALL, '') - For Windows
  sales = 0
  max_revenue = {"revenue": 0}
  most_popular_year = {}

  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if (item["total_sales"] > sales ):
       sales= item["total_sales"]
       max_sales = item

   # TODO: also handle most popular car_year
  for item in data:
    year=(get_year(item["car"]))
    most_popular_year[year]= most_popular_year.get(year,0) + item["total_sales"]
  summary = [
    "The {} generated the most revenue: ${}".format(format_car(max_revenue["car$
    "The {} car model had the most sales: {}".format(format_car(max_sales["car"$
    "The most popular year was ({}) with {} sales.".format (max(most_popular_ye$
    ]
  return summary

def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item$
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  summary = process_data(data)
  full_summary_file= summary[0] + "<br/>" +  summary[1] + "<br/>" + summary[2] $
  full_summary_body = summary[0] + "\n" +  summary[1] + "\n" + summary[2] + "\n"
  # TODO: turn this into a PDF report
  reports.generate( "/tmp/cars.pdf","Sales summary for last Month",full_summary$
  # TODO: send the PDF report as an email attachment
  message=emails.generate("automation@example.com","student-00-28a938f27d45@exa$
  emails.send=emails.send(message)


if __name__ == "__main__":
  main(sys.argv)






  
