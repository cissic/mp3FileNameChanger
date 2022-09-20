from mp3_tagger import MP3File


import os

# Get the list of all files and directories
# in the root directory
path = "/path/to/directory/with/directories/of/albums"
dir_list = os.listdir(path)

# print("Files and directories in '", path, "' :") 
# print the list
# print(dir_list)


for albumFolder in dir_list:
    # print(album)
    
    file_list = os.listdir(path+albumFolder)
    
    for file in file_list:
        
        # check only mp3 files
        if file.endswith('.mp3'):
            mp3filename = file 
            
            #print(mp3filename)
            
            
            mp3Instance = MP3File(path+albumFolder+'/'+mp3filename)
            
            tags = mp3Instance.get_tags()
            #print(tags) 
            # tagToBeRead = 'ID3TagV1' # shorter names! It's better to use TagV2
            tagToBeRead = 'ID3TagV2' # 
            
            #print(tags[tagToBeRead])
            #print(tags[tagToBeRead]['artist'])
            #print(tags[tagToBeRead]['album'])
            #print(tags[tagToBeRead]['track'])
            #print(tags[tagToBeRead]['song'])
            
            artist = tags[tagToBeRead]['artist']
            album  = tags[tagToBeRead]['album']
            year   = tags['ID3TagV1']['year']      # TagV2 stores year with month and day
            track  = tags[tagToBeRead]['track']
            song   = str(tags[tagToBeRead]['song'])

            
            
            trackNo  = int(track)
            if trackNo < 10:
                track = str('0'+track)                
            
            if '/' in song:
                newsong = song.replace("/", "-")
                song = newsong
                
            if '"' in song:
                newsong = song.replace('"', "''")
                song = newsong 
            if ':' in song:
                newsong = song.replace(':', "-")
                song = newsong                      

                
            # new_mp3FileName = track+'. '+artist + ' - ' + song
            new_mp3FileName = track+'. '+ str(song) + '.mp3'
            os.rename(str(path+albumFolder+'/'+mp3filename), str(path+albumFolder+'/'+new_mp3FileName) )
            print(str(path+albumFolder+'/'+new_mp3FileName) )


    if ':' in album:
        newalbum = album.replace(':', "-")
        album = newalbum

    new_FolderName = artist+ ' [' + year + '] - '+ album
    os.rename(path+albumFolder, path+new_FolderName )
    print(new_FolderName)
            
    #break 
