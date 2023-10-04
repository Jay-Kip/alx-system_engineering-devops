#!/usr/bin/env ruby
#puts ARGV[0].scan(/\[(from:)(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join
input = ARGV[0]
pattern = /\[(from:)(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/

match_data = input.match(pattern)

if match_data
  sender = match_data[1]
  reciever = match_data[2]
  flags = match_data[3]
  sender.gsub!('from:','')
  puts "#{sender},#{reciever},#{flags}"
else
  puts "No match found"
end
