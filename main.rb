require 'sinatra'
require 'json'


get '/' do
	erb :index
end

post '/update' do

	data = JSON.parse(request.body.read)	

	file = File.new("spam.txt", "w")
	file.puts(data.first["spam"])
	file.close

	file = File.new("notSpam.txt", "w")
	file.puts(data.first["notSpam"])
	file.close
end