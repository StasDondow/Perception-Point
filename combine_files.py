import pandas as pd

filenames = {
	"Lionel Messi": "data/messi.csv", 
	"Cristiano Ronaldo": "data/ronaldo.csv", 
	"Neymar": "data/neymar.csv", 
	"Robert Lewandowski": "data/lewandowski.csv"}


combined_data = pd.DataFrame()

for player, filename in filenames.items():
	data = pd.read_csv(filename)
	data["Player"] = player
	combined_data = pd.concat([combined_data, data], ignore_index=True)

combined_data.to_csv("data/combined_data.csv", index=False)
