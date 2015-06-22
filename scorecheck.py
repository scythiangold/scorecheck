from music21 import *

# sBach = corpus.parse('bach/bwv57.8')

print(search.segment.getDifflibOrPyLev())

# searchResults = corpus.search('bwv19')
# fpsNamesOnly = sorted([searchResult.sourcePath for searchResult in searchResults])
# print(len(fpsNamesOnly))

# scoreDict = search.segment.indexScoreFilePaths(fpsNamesOnly[2:5])
# print(len(scoreDict['bwv190.7.mxl']))

# print(scoreDict['bwv190.7.mxl'][0]['measureList'])

# print(scoreDict['bwv190.7.mxl'][0]['segmentList'][0])

# bach = corpus.parse('bwv66.6')

filePath1 = '/Users/ryan/Documents/Francis Cabrel - Je Laime A Mourir 1.xml'
filePath2 = '/Users/ryan/Documents/Francis Cabrel - Je Laime A Mourir 2.xml'
filePath3 = '/Users/ryan/Documents/Francis Cabrel - Je Laime A Mourir 3.xml'
cabrel1 = converter.parse(filePath1)
cabrel2 = converter.parse(filePath2)
cabrel3 = converter.parse(filePath3)

# for j in range(2):
#     file = midi.MidiFile()
#     file.open(filePath)
#     file.read()
#     a = len(file.tracks)
#     for i in range(a):
#         track = file.tracks[i]
#         channel = track.getChannels()
#         if channel[1] == 10:
#             track.events = []
#     score = converter.parseData(file.writestr())
#     # score = score.implode()
#     # score = score.flattenParts()
#     scoreChords = score.chordify()
#     score = scoreChords.flat
#     # b = len(score.)
#     # for k in range(b):
#     #     closedChord = chord.semiClosedPosition()
#     if j == 0:
#         origScore = score
#         filePath2 = filePath
#     else:
#         dbScore = score
#
#     filePath = '/Users/ryan/Documents/Francis Cabrel - Je Laime A Mourir (Pro).mid'

# origScore.show()
# dbScore.show()

scoreChords = cabrel1.chordify()
score = scoreChords.flat
cabrel1 = score
scoreChords = cabrel2.chordify()
score = scoreChords.flat
cabrel2 = score
scoreChords = cabrel3
score = scoreChords.flat
cabrel3 = score

cabrel1.show()
cabrel2.show()
cabrel3.show()

c = converter.subConverters.ConverterMusicXML()
cabrel4 = musicxml.m21ToString.fromStream(cabrel1)
cabrel5 = musicxml.m21ToString.fromStream(cabrel2)
cabrel6 = musicxml.m21ToString.fromStream(cabrel3)
c.writeDataStream('/Users/ryan/Documents/cabrel1.mxl', cabrel4);
c.writeDataStream('/Users/ryan/Documents/cabrel2.mxl', cabrel5);
c.writeDataStream('/Users/ryan/Documents/cabrel3.mxl', cabrel6);
filePath4 = '/Users/ryan/Documents/cabrel1.mxl'
filePath5 = '/Users/ryan/Documents/cabrel2.mxl'
filePath6 = '/Users/ryan/Documents/cabrel3.mxl'

#converter.subConverters.SubConverter.writeDataStream(c, cabrel, cabrel)
#converter.subConverters.ConverterMusicXML.write(c)
# x = cabrel.read(cabrel, audit=False)

# c = converter.subConverters.ConverterMusicXML
# s = c.parseData(cabrel)
# print(s)
# converter.subConverters.ConverterMusicXML.load()
# converter.subConverters.ConverterMusicXML.write(s)

# print(converter.subConverters.SubConverter.checkShowAbility('musicxml'))
# converter.subConverters.SubConverter.stream = cabrel1
# print(converter.subConverters.SubConverter.stream)

# music21.midi.translate.streamHierarchyToMidiTracks(inputM21, acceptableChannelList=None)
# music21.midi.translate.streamToMidiFile(inputM21)

# >>> s = stream.Stream()
# >>> n = note.Note('g#')
# >>> n.quarterLength = .5
# >>> s.repeatAppend(n, 4)
# >>> mf = midi.translate.streamToMidiFile(s)
# >>> len(mf.tracks)
# 1
# >>> len(mf.tracks[0].events)
# 22
#
# From here, you can call mf.writestr() to get the actual file info.
# >>>
#
# >>> sc = scale.PhrygianScale('g')
# >>> s = stream.Stream()
# >>> x=[s.append(note.Note(sc.pitchFromDegree(i % 11), quarterLength=.25)) for i in range(60)]
# >>> mf = midi.translate.streamToMidiFile(s)
# >>> mf.open('/Volumes/xdisc/_scratch/midi.mid', 'wb')
# >>> mf.write()
# >>> mf.close()



# music21.midi.translate.midiFileToStream(mf, inputM21=None, quantizePost=True)
#
#     Convert a MidiFile object to a Stream object.
#
#     The inputM21 object can specify an existing Stream (or Stream subclass) to fill.
#     >>>
#
#     >>> import os
#     >>> fp = os.path.join(common.getSourceFilePath(), 'midi', 'testPrimitive',  'test05.mid')
#     >>> mf = midi.MidiFile()
#     >>> mf.open(fp)
#     >>> mf.read()
#     >>> mf.close()
#     >>> len(mf.tracks)
#     1
#     >>> s = midi.translate.midiFileToStream(mf)
#     >>> s
#     <music21.stream.Score ...>
#     >>> len(s.flat.notesAndRests)
#     11



# cabrel = converter.subConverters.SubConverter.parseFile(filePath1)
# cabrel = converter.subConverters.SubConverter.parseFile(filePath1)
# cabrel = converter.subConverters.SubConverter.parseFile(filePath1)

# converter.subConverters.SubConverter.writeDataStream(cabrel, cabrel)
# converter.subConverters.ConverterMusicXML.write(1, musicxml, fp='cabrel.mxl', subformats=None)

filePaths = []
filePaths.append(filePath4)
filePaths.append(filePath5)
filePaths.append(filePath6)
# filePaths.append(corpus.search('bwv197.5.mxl')[0].sourcePath)
# filePaths.append(corpus.search('bwv190.7.mxl')[0].sourcePath)
# filePaths.append(corpus.search('bwv197.10.mxl')[0].sourcePath)
scoreDict = search.segment.indexScoreFilePaths(filePaths)

# scoreList = search.segment.indexScoreParts(scoreDict)
# print(scoreList[1]['segmentList'][0])
# print(scoreList[1]['measureList'][0:3])

# search.segment.saveScoreDict(scoreDict, filePath=None)
# search.segment.loadScoreDict(filePath)

scoreSim = search.segment.scoreSimilarity(scoreDict)
print(len(scoreSim))
scoreTotal = [0, 0]
scoreLength = [0, 0]
scoreAverage = [0, 0]

# i = 6764
# k =
print(filePaths[0])
print(filePaths[1])
print(filePaths[2])
j = (len(filePaths) - 1)


for result in scoreSim:
    print(result[4])
    if result[4] == 'cabrel2.mxl':
        scoreTotal[0] = result[8] + scoreTotal[0]
        scoreLength[0] = scoreLength[0] + 1
    if result[4] == 'cabrel3.mxl':
        scoreTotal[1] = result[8] + scoreTotal[1]
        scoreLength[1] = scoreLength[1] + 1
    # if result[4] == 'bwv197.10.mxl':
    #     scoreTotal[2] = result[8] + scoreTotal[2]
    #     scoreLength[2] = scoreLength[2] + 1
print(scoreLength[0])
print(scoreLength[1])
scoreAverage[0] = scoreTotal[0] / scoreLength[0]
scoreAverage[1] = scoreTotal[1] / scoreLength[1]
# scoreAverage[2] = scoreTotal[2] / scoreLength[2]
print('cabrel2.xml')
print(scoreAverage[0] * 100)
print('cabrel3.xml')
print(scoreAverage[1] * 100)
# print('bwv197.10.mxl')
# print(scoreAverage[2] * 100)