import variables

root = 'http://ws.audioscrobbler.com/2.0/'
api_key = f'&api_key={variables.API_KEY}'
json = '&format=json'
limit = f'&limit='

chart = f'{root}?method=chart.'
top_artist = f'{chart}getTopArtists{api_key}'
