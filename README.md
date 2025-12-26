# MINIMAX (HaiLuo) TTS Home-Assistant Custom-Component

## Prerequisite

API Key from Hailuo AI

International https://intl.minimaxi.com/

China https://platform.minimaxi.com/

## Features

| Support Languages |               |               |
| ----------------- | ------------- | ------------- |
| 1. Chinese        | 15. Turkish   | 28. Malay     |
| 2. Cantonese      | 16. Dutch     | 29. Persian   |
| 3. English        | 17. Ukrainian | 30. Slovak    |
| 4. Spanish        | 18. Thai      | 31. Swedish   |
| 5. French         | 19. Polish    | 32. Croatian  |
| 6. Russian        | 20. Romanian  | 33. Filipino  |
| 7. German         | 21. Greek     | 34. Hungarian |
| 8. Portuguese     | 22. Czech     | 35. Norwegian |
| 9. Arabic         | 23. Finnish   | 36. Slovenian |
| 10. Italian       | 24. Hindi     | 37. Catalan   |
| 11. Japanese      | 25. Bulgarian | 38. Nynorsk   |
| 12. Korean        | 26. Danish    | 39. Tamil     |
| 13. Indonesian    | 27. Hebrew    | 40. Afrikaans |
| 14. Vietnamese    |               |               |

| Model            | Description                                                                                              |
| ---------------- | -------------------------------------------------------------------------------------------------------- |
| speech-2.6-hd    | Ultra-low latency, intelligence parsing, and enhanced naturalness.                                       |
| speech-2.6-turbo | Faster, more affordable, and ideal for your agent.                                                       |
| speech-02-hd     | Superior rhythm and stability, with outstanding performance in replication similarity and sound quality. |
| speech-02-turbo  | Superior rhythm and stability, with enhanced multilingual capabilities and excellent performance.        |


| No. | Language           | Voice\_id                                    | Voice\_name               |
| :-- | :----------------- | :------------------------------------------- | :------------------------ |
| 1   | English            | English\_expressive\_narrator                | Expressive Narrator       |
| 2   | English            | English\_radiant\_girl                       | Radiant Girl              |
| 3   | English            | English\_magnetic\_voiced\_man               | Magnetic-voiced Male      |
| 4   | English            | English\_compelling\_lady1                   | Compelling Lady           |
| 5   | English            | English\_Aussie\_Bloke                       | Aussie Bloke              |
| 6   | English            | English\_captivating\_female1                | Captivating Female        |
| 7   | English            | English\_Upbeat\_Woman                       | Upbeat Woman              |
| 8   | English            | English\_Trustworth\_Man                     | Trustworthy Man           |
| 9   | English            | English\_CalmWoman                           | Calm Woman                |
| 10  | English            | English\_UpsetGirl                           | Upset Girl                |
| 11  | English            | English\_Gentle-voiced\_man                  | Gentle-voiced Man         |
| 12  | English            | English\_Whispering\_girl                    | Whispering girl           |
| 13  | English            | English\_Diligent\_Man                       | Diligent Man              |
| 14  | English            | English\_Graceful\_Lady                      | Graceful Lady             |
| 15  | English            | English\_ReservedYoungMan                    | Reserved Young Man        |
| 16  | English            | English\_PlayfulGirl                         | Playful Girl              |
| 17  | English            | English\_ManWithDeepVoice                    | Man With Deep Voice       |
| 18  | English            | English\_MaturePartner                       | Mature Partner            |
| 19  | English            | English\_FriendlyPerson                      | Friendly Guy              |
| 20  | English            | English\_MatureBoss                          | Bossy Lady                |
| 21  | English            | English\_Debator                             | Male Debater              |
| 22  | English            | English\_LovelyGirl                          | Lovely Girl               |
| 23  | English            | English\_Steadymentor                        | Reliable Man              |
| 24  | English            | English\_Deep-VoicedGentleman                | Deep-voiced Gentleman     |
| 25  | English            | English\_Wiselady                            | Wise Lady                 |
| 26  | English            | English\_CaptivatingStoryteller              | Captivating Storyteller   |
| 27  | English            | English\_DecentYoungMan                      | Decent Young Man          |
| 28  | English            | English\_SentimentalLady                     | Sentimental Lady          |
| 29  | English            | English\_ImposingManner                      | Imposing Queen            |
| 30  | English            | English\_SadTeen                             | Teen Boy                  |
| 31  | English            | English\_PassionateWarrior                   | Passionate Warrior        |
| 32  | English            | English\_WiseScholar                         | Wise Scholar              |
| 33  | English            | English\_Soft-spokenGirl                     | Soft-Spoken Girl          |
| 34  | English            | English\_SereneWoman                         | Serene Woman              |
| 35  | English            | English\_ConfidentWoman                      | Confident Woman           |
| 36  | English            | English\_PatientMan                          | Patient Man               |
| 37  | English            | English\_Comedian                            | Comedian                  |
| 38  | English            | English\_BossyLeader                         | Bossy Leader              |
| 39  | English            | English\_Strong-WilledBoy                    | Strong-Willed Boy         |
| 40  | English            | English\_StressedLady                        | Stressed Lady             |
| 41  | English            | English\_AssertiveQueen                      | Assertive Queen           |
| 42  | English            | English\_AnimeCharacter                      | Female Narrator           |
| 43  | English            | English\_Jovialman                           | Jovial Man                |
| 44  | English            | English\_WhimsicalGirl                       | Whimsical Girl            |
| 45  | English            | English\_Kind-heartedGirl                    | Kind-Hearted Girl         |
| 46  | Chinese (Mandarin) | Chinese (Mandarin)\_Reliable\_Executive      | Reliable Executive        |
| 47  | Chinese (Mandarin) | Chinese (Mandarin)\_News\_Anchor             | News Anchor               |
| 48  | Chinese (Mandarin) | Chinese (Mandarin)\_Unrestrained\_Young\_Man | Unrestrained Young Man    |
| 49  | Chinese (Mandarin) | Chinese (Mandarin)\_Mature\_Woman            | Mature Woman              |
| 50  | Chinese (Mandarin) | Arrogant\_Miss                               | Arrogant Miss             |
| 51  | Chinese (Mandarin) | Robot\_Armor                                 | Robot Armor               |
| 52  | Chinese (Mandarin) | Chinese (Mandarin)\_Kind-hearted\_Antie      | Kind-hearted Antie        |
| 53  | Chinese (Mandarin) | Chinese (Mandarin)\_HK\_Flight\_Attendant    | HK Flight Attendant       |
| 54  | Chinese (Mandarin) | Chinese (Mandarin)\_Humorous\_Elder          | Humorous Elder            |
| 55  | Chinese (Mandarin) | Chinese (Mandarin)\_Gentleman                | Gentleman                 |
| 56  | Chinese (Mandarin) | Chinese (Mandarin)\_Warm\_Bestie             | Warm Bestie               |
| 57  | Chinese (Mandarin) | Chinese (Mandarin)\_Stubborn\_Friend         | Stubborn Friend           |
| 58  | Chinese (Mandarin) | Chinese (Mandarin)\_Sweet\_Lady              | Sweet Lady                |
| 59  | Chinese (Mandarin) | Chinese (Mandarin)\_Southern\_Young\_Man     | Southern Young Man        |
| 60  | Chinese (Mandarin) | Chinese (Mandarin)\_Wise\_Women              | Wise Women                |
| 61  | Chinese (Mandarin) | Chinese (Mandarin)\_Gentle\_Youth            | Gentle Youth              |
| 62  | Chinese (Mandarin) | Chinese (Mandarin)\_Warm\_Girl               | Warm Girl                 |
| 63  | Chinese (Mandarin) | Chinese (Mandarin)\_Male\_Announcer          | Male Announcer            |
| 64  | Chinese (Mandarin) | Chinese (Mandarin)\_Kind-hearted\_Elder      | Kind-hearted Elder        |
| 65  | Chinese (Mandarin) | Chinese (Mandarin)\_Cute\_Spirit             | Cute Spirit               |
| 66  | Chinese (Mandarin) | Chinese (Mandarin)\_Radio\_Host              | Radio Host                |
| 67  | Chinese (Mandarin) | Chinese (Mandarin)\_Lyrical\_Voice           | Lyrical Voice             |
| 68  | Chinese (Mandarin) | Chinese (Mandarin)\_Straightforward\_Boy     | Straightforward Boy       |
| 69  | Chinese (Mandarin) | Chinese (Mandarin)\_Sincere\_Adult           | Sincere Adult             |
| 70  | Chinese (Mandarin) | Chinese (Mandarin)\_Gentle\_Senior           | Gentle Senior             |
| 71  | Chinese (Mandarin) | Chinese (Mandarin)\_Crisp\_Girl              | Crisp Girl                |
| 72  | Chinese (Mandarin) | Chinese (Mandarin)\_Pure-hearted\_Boy        | Pure-hearted Boy          |
| 73  | Chinese (Mandarin) | Chinese (Mandarin)\_Soft\_Girl               | Soft Girl                 |
| 74  | Chinese (Mandarin) | Chinese (Mandarin)\_IntellectualGirl         | Intellectual Girl         |
| 75  | Chinese (Mandarin) | Chinese (Mandarin)\_Warm\_HeartedGirl        | Warm-hearted Girl         |
| 76  | Chinese (Mandarin) | Chinese (Mandarin)\_Laid\_BackGirl           | Laid-back Girl            |
| 77  | Chinese (Mandarin) | Chinese (Mandarin)\_ExplorativeGirl          | Explorative Girl          |
| 78  | Chinese (Mandarin) | Chinese (Mandarin)\_Warm-HeartedAunt         | Warm-hearted Aunt         |
| 79  | Chinese (Mandarin) | Chinese (Mandarin)\_BashfulGirl              | Bashful Girl              |
| 80  | Japanese           | Japanese\_IntellectualSenior                 | Intellectual Senior       |
| 81  | Japanese           | Japanese\_DecisivePrincess                   | Decisive Princess         |
| 82  | Japanese           | Japanese\_LoyalKnight                        | Loyal Knight              |
| 83  | Japanese           | Japanese\_DominantMan                        | Dominant Man              |
| 84  | Japanese           | Japanese\_SeriousCommander                   | Serious Commander         |
| 85  | Japanese           | Japanese\_ColdQueen                          | Cold Queen                |
| 86  | Japanese           | Japanese\_DependableWoman                    | Dependable Woman          |
| 87  | Japanese           | Japanese\_GentleButler                       | Gentle Butler             |
| 88  | Japanese           | Japanese\_KindLady                           | Kind Lady                 |
| 89  | Japanese           | Japanese\_CalmLady                           | Calm Lady                 |
| 90  | Japanese           | Japanese\_OptimisticYouth                    | Optimistic Youth          |
| 91  | Japanese           | Japanese\_GenerousIzakayaOwner               | Generous Izakaya Owner    |
| 92  | Japanese           | Japanese\_SportyStudent                      | Sporty Student            |
| 93  | Japanese           | Japanese\_InnocentBoy                        | Innocent Boy              |
| 94  | Japanese           | Japanese\_GracefulMaiden                     | Graceful Maiden           |
| 95  | Cantonese          | Cantonese\_ProfessionalHost (F)              | Professional Female Host  |
| 96  | Cantonese          | Cantonese\_GentleLady                        | Gentle Lady               |
| 97  | Cantonese          | Cantonese\_ProfessionalHost (M)              | Professional Male Host    |
| 98  | Cantonese          | Cantonese\_PlayfulMan                        | Playful Man               |
| 99  | Cantonese          | Cantonese\_CuteGirl                          | Cute Girl                 |
| 100 | Cantonese          | Cantonese\_KindWoman                         | Kind Woman                |
| 101 | Korean             | Korean\_AirheadedGirl                        | Airheaded Girl            |
| 102 | Korean             | Korean\_AthleticGirl                         | Athletic Girl             |
| 103 | Korean             | Korean\_AthleticStudent                      | Athletic Student          |
| 104 | Korean             | Korean\_BraveAdventurer                      | Brave Adventurer          |
| 105 | Korean             | Korean\_BraveFemaleWarrior                   | Brave Female Warrior      |
| 106 | Korean             | Korean\_BraveYouth                           | Brave Youth               |
| 107 | Korean             | Korean\_CalmGentleman                        | Calm Gentleman            |
| 108 | Korean             | Korean\_CalmLady                             | Calm Lady                 |
| 109 | Korean             | Korean\_CaringWoman                          | Caring Woman              |
| 110 | Korean             | Korean\_CharmingElderSister                  | Charming Elder Sister     |
| 111 | Korean             | Korean\_CharmingSister                       | Charming Sister           |
| 112 | Korean             | Korean\_CheerfulBoyfriend                    | Cheerful Boyfriend        |
| 113 | Korean             | Korean\_CheerfulCoolJunior                   | Cheerful Cool Junior      |
| 114 | Korean             | Korean\_CheerfulLittleSister                 | Cheerful Little Sister    |
| 115 | Korean             | Korean\_ChildhoodFriendGirl                  | Childhood Friend Girl     |
| 116 | Korean             | Korean\_CockyGuy                             | Cocky Guy                 |
| 117 | Korean             | Korean\_ColdGirl                             | Cold Girl                 |
| 118 | Korean             | Korean\_ColdYoungMan                         | Cold Young Man            |
| 119 | Korean             | Korean\_ConfidentBoss                        | Confident Boss            |
| 120 | Korean             | Korean\_ConsiderateSenior                    | Considerate Senior        |
| 121 | Korean             | Korean\_DecisiveQueen                        | Decisive Queen            |
| 122 | Korean             | Korean\_DominantMan                          | Dominant Man              |
| 123 | Korean             | Korean\_ElegantPrincess                      | Elegant Princess          |
| 124 | Korean             | Korean\_EnchantingSister                     | Enchanting Sister         |
| 125 | Korean             | Korean\_EnthusiasticTeen                     | Enthusiastic Teen         |
| 126 | Korean             | Korean\_FriendlyBigSister                    | Friendly Big Sister       |
| 127 | Korean             | Korean\_GentleBoss                           | Gentle Boss               |
| 128 | Korean             | Korean\_GentleWoman                          | Gentle Woman              |
| 129 | Korean             | Korean\_HaughtyLady                          | Haughty Lady              |
| 130 | Korean             | Korean\_InnocentBoy                          | Innocent Boy              |
| 131 | Korean             | Korean\_IntellectualMan                      | Intellectual Man          |
| 132 | Korean             | Korean\_IntellectualSenior                   | Intellectual Senior       |
| 133 | Korean             | Korean\_LonelyWarrior                        | Lonely Warrior            |
| 134 | Korean             | Korean\_MatureLady                           | Mature Lady               |
| 135 | Korean             | Korean\_MysteriousGirl                       | Mysterious Girl           |
| 136 | Korean             | Korean\_OptimisticYouth                      | Optimistic Youth          |
| 137 | Korean             | Korean\_PlayboyCharmer                       | Playboy Charmer           |
| 138 | Korean             | Korean\_PossessiveMan                        | Possessive Man            |
| 139 | Korean             | Korean\_QuirkyGirl                           | Quirky Girl               |
| 140 | Korean             | Korean\_ReliableSister                       | Reliable Sister           |
| 141 | Korean             | Korean\_ReliableYouth                        | Reliable Youth            |
| 142 | Korean             | Korean\_SassyGirl                            | Sassy Girl                |
| 143 | Korean             | Korean\_ShyGirl                              | Shy Girl                  |
| 144 | Korean             | Korean\_SoothingLady                         | Soothing Lady             |
| 145 | Korean             | Korean\_StrictBoss                           | Strict Boss               |
| 146 | Korean             | Korean\_SweetGirl                            | Sweet Girl                |
| 147 | Korean             | Korean\_ThoughtfulWoman                      | Thoughtful Woman          |
| 148 | Korean             | Korean\_WiseElf                              | Wise Elf                  |
| 149 | Korean             | Korean\_WiseTeacher                          | Wise Teacher              |
| 150 | Spanish            | Spanish\_SereneWoman                         | Serene Woman              |
| 151 | Spanish            | Spanish\_MaturePartner                       | Mature Partner            |
| 152 | Spanish            | Spanish\_CaptivatingStoryteller              | Captivating Storyteller   |
| 153 | Spanish            | Spanish\_Narrator                            | Narrator                  |
| 154 | Spanish            | Spanish\_WiseScholar                         | Wise Scholar              |
| 155 | Spanish            | Spanish\_Kind-heartedGirl                    | Kind-hearted Girl         |
| 156 | Spanish            | Spanish\_DeterminedManager                   | Determined Manager        |
| 157 | Spanish            | Spanish\_BossyLeader                         | Bossy Leader              |
| 158 | Spanish            | Spanish\_ReservedYoungMan                    | Reserved Young Man        |
| 159 | Spanish            | Spanish\_ConfidentWoman                      | Confident Woman           |
| 160 | Spanish            | Spanish\_ThoughtfulMan                       | Thoughtful Man            |
| 161 | Spanish            | Spanish\_Strong-WilledBoy                    | Strong-willed Boy         |
| 162 | Spanish            | Spanish\_SophisticatedLady                   | Sophisticated Lady        |
| 163 | Spanish            | Spanish\_RationalMan                         | Rational Man              |
| 164 | Spanish            | Spanish\_AnimeCharacter                      | Anime Character           |
| 165 | Spanish            | Spanish\_Deep-tonedMan                       | Deep-toned Man            |
| 166 | Spanish            | Spanish\_Fussyhostess                        | Fussy hostess             |
| 167 | Spanish            | Spanish\_SincereTeen                         | Sincere Teen              |
| 168 | Spanish            | Spanish\_FrankLady                           | Frank Lady                |
| 169 | Spanish            | Spanish\_Comedian                            | Comedian                  |
| 170 | Spanish            | Spanish\_Debator                             | Debator                   |
| 171 | Spanish            | Spanish\_ToughBoss                           | Tough Boss                |
| 172 | Spanish            | Spanish\_Wiselady                            | Wise Lady                 |
| 173 | Spanish            | Spanish\_Steadymentor                        | Steady Mentor             |
| 174 | Spanish            | Spanish\_Jovialman                           | Jovial Man                |
| 175 | Spanish            | Spanish\_SantaClaus                          | Santa Claus               |
| 176 | Spanish            | Spanish\_Rudolph                             | Rudolph                   |
| 177 | Spanish            | Spanish\_Intonategirl                        | Intonate Girl             |
| 178 | Spanish            | Spanish\_Arnold                              | Arnold                    |
| 179 | Spanish            | Spanish\_Ghost                               | Ghost                     |
| 180 | Spanish            | Spanish\_HumorousElder                       | Humorous Elder            |
| 181 | Spanish            | Spanish\_EnergeticBoy                        | Energetic Boy             |
| 182 | Spanish            | Spanish\_WhimsicalGirl                       | Whimsical Girl            |
| 183 | Spanish            | Spanish\_StrictBoss                          | Strict Boss               |
| 184 | Spanish            | Spanish\_ReliableMan                         | Reliable Man              |
| 185 | Spanish            | Spanish\_SereneElder                         | Serene Elder              |
| 186 | Spanish            | Spanish\_AngryMan                            | Angry Man                 |
| 187 | Spanish            | Spanish\_AssertiveQueen                      | Assertive Queen           |
| 188 | Spanish            | Spanish\_CaringGirlfriend                    | Caring Girlfriend         |
| 189 | Spanish            | Spanish\_PowerfulSoldier                     | Powerful Soldier          |
| 190 | Spanish            | Spanish\_PassionateWarrior                   | Passionate Warrior        |
| 191 | Spanish            | Spanish\_ChattyGirl                          | Chatty Girl               |
| 192 | Spanish            | Spanish\_RomanticHusband                     | Romantic Husband          |
| 193 | Spanish            | Spanish\_CompellingGirl                      | Compelling Girl           |
| 194 | Spanish            | Spanish\_PowerfulVeteran                     | Powerful Veteran          |
| 195 | Spanish            | Spanish\_SensibleManager                     | Sensible Manager          |
| 196 | Spanish            | Spanish\_ThoughtfulLady                      | Thoughtful Lady           |
| 197 | Portuguese         | Portuguese\_SentimentalLady                  | Sentimental Lady          |
| 198 | Portuguese         | Portuguese\_BossyLeader                      | Bossy Leader              |
| 199 | Portuguese         | Portuguese\_Wiselady                         | Wise lady                 |
| 200 | Portuguese         | Portuguese\_Strong-WilledBoy                 | Strong-willed Boy         |
| 201 | Portuguese         | Portuguese\_Deep-VoicedGentleman             | Deep-voiced Gentleman     |
| 202 | Portuguese         | Portuguese\_UpsetGirl                        | Upset Girl                |
| 203 | Portuguese         | Portuguese\_PassionateWarrior                | Passionate Warrior        |
| 204 | Portuguese         | Portuguese\_AnimeCharacter                   | Anime Character           |
| 205 | Portuguese         | Portuguese\_ConfidentWoman                   | Confident Woman           |
| 206 | Portuguese         | Portuguese\_AngryMan                         | Angry Man                 |
| 207 | Portuguese         | Portuguese\_CaptivatingStoryteller           | Captivating Storyteller   |
| 208 | Portuguese         | Portuguese\_Godfather                        | Godfather                 |
| 209 | Portuguese         | Portuguese\_ReservedYoungMan                 | Reserved Young Man        |
| 210 | Portuguese         | Portuguese\_SmartYoungGirl                   | Smart Young Girl          |
| 211 | Portuguese         | Portuguese\_Kind-heartedGirl                 | Kind-hearted Girl         |
| 212 | Portuguese         | Portuguese\_Pompouslady                      | Pompous lady              |
| 213 | Portuguese         | Portuguese\_Grinch                           | Grinch                    |
| 214 | Portuguese         | Portuguese\_Debator                          | Debator                   |
| 215 | Portuguese         | Portuguese\_SweetGirl                        | Sweet Girl                |
| 216 | Portuguese         | Portuguese\_AttractiveGirl                   | Attractive Girl           |
| 217 | Portuguese         | Portuguese\_ThoughtfulMan                    | Thoughtful Man            |
| 218 | Portuguese         | Portuguese\_PlayfulGirl                      | Playful Girl              |
| 219 | Portuguese         | Portuguese\_GorgeousLady                     | Gorgeous Lady             |
| 220 | Portuguese         | Portuguese\_LovelyLady                       | Lovely Lady               |
| 221 | Portuguese         | Portuguese\_SereneWoman                      | Serene Woman              |
| 222 | Portuguese         | Portuguese\_SadTeen                          | Sad Teen                  |
| 223 | Portuguese         | Portuguese\_MaturePartner                    | Mature Partner            |
| 224 | Portuguese         | Portuguese\_Comedian                         | Comedian                  |
| 225 | Portuguese         | Portuguese\_NaughtySchoolgirl                | Naughty Schoolgirl        |
| 226 | Portuguese         | Portuguese\_Narrator                         | Narrator                  |
| 227 | Portuguese         | Portuguese\_ToughBoss                        | Tough Boss                |
| 228 | Portuguese         | Portuguese\_Fussyhostess                     | Fussy hostess             |
| 229 | Portuguese         | Portuguese\_Dramatist                        | Dramatist                 |
| 230 | Portuguese         | Portuguese\_Steadymentor                     | Steady Mentor             |
| 231 | Portuguese         | Portuguese\_Jovialman                        | Jovial Man                |
| 232 | Portuguese         | Portuguese\_CharmingQueen                    | Charming Queen            |
| 233 | Portuguese         | Portuguese\_SantaClaus                       | Santa Claus               |
| 234 | Portuguese         | Portuguese\_Rudolph                          | Rudolph                   |
| 235 | Portuguese         | Portuguese\_Arnold                           | Arnold                    |
| 236 | Portuguese         | Portuguese\_CharmingSanta                    | Charming Santa            |
| 237 | Portuguese         | Portuguese\_CharmingLady                     | Charming Lady             |
| 238 | Portuguese         | Portuguese\_Ghost                            | Ghost                     |
| 239 | Portuguese         | Portuguese\_HumorousElder                    | Humorous Elder            |
| 240 | Portuguese         | Portuguese\_CalmLeader                       | Calm Leader               |
| 241 | Portuguese         | Portuguese\_GentleTeacher                    | Gentle Teacher            |
| 242 | Portuguese         | Portuguese\_EnergeticBoy                     | Energetic Boy             |
| 243 | Portuguese         | Portuguese\_ReliableMan                      | Reliable Man              |
| 244 | Portuguese         | Portuguese\_SereneElder                      | Serene Elder              |
| 245 | Portuguese         | Portuguese\_GrimReaper                       | Grim Reaper               |
| 246 | Portuguese         | Portuguese\_AssertiveQueen                   | Assertive Queen           |
| 247 | Portuguese         | Portuguese\_WhimsicalGirl                    | Whimsical Girl            |
| 248 | Portuguese         | Portuguese\_StressedLady                     | Stressed Lady             |
| 249 | Portuguese         | Portuguese\_FriendlyNeighbor                 | Friendly Neighbor         |
| 250 | Portuguese         | Portuguese\_CaringGirlfriend                 | Caring Girlfriend         |
| 251 | Portuguese         | Portuguese\_PowerfulSoldier                  | Powerful Soldier          |
| 252 | Portuguese         | Portuguese\_FascinatingBoy                   | Fascinating Boy           |
| 253 | Portuguese         | Portuguese\_RomanticHusband                  | Romantic Husband          |
| 254 | Portuguese         | Portuguese\_StrictBoss                       | Strict Boss               |
| 255 | Portuguese         | Portuguese\_InspiringLady                    | Inspiring Lady            |
| 256 | Portuguese         | Portuguese\_PlayfulSpirit                    | Playful Spirit            |
| 257 | Portuguese         | Portuguese\_ElegantGirl                      | Elegant Girl              |
| 258 | Portuguese         | Portuguese\_CompellingGirl                   | Compelling Girl           |
| 259 | Portuguese         | Portuguese\_PowerfulVeteran                  | Powerful Veteran          |
| 260 | Portuguese         | Portuguese\_SensibleManager                  | Sensible Manager          |
| 261 | Portuguese         | Portuguese\_ThoughtfulLady                   | Thoughtful Lady           |
| 262 | Portuguese         | Portuguese\_TheatricalActor                  | Theatrical Actor          |
| 263 | Portuguese         | Portuguese\_FragileBoy                       | Fragile Boy               |
| 264 | Portuguese         | Portuguese\_ChattyGirl                       | Chatty Girl               |
| 265 | Portuguese         | Portuguese\_Conscientiousinstructor          | Conscientious Instructor  |
| 266 | Portuguese         | Portuguese\_RationalMan                      | Rational Man              |
| 267 | Portuguese         | Portuguese\_WiseScholar                      | Wise Scholar              |
| 268 | Portuguese         | Portuguese\_FrankLady                        | Frank Lady                |
| 269 | Portuguese         | Portuguese\_DeterminedManager                | Determined Manager        |
| 270 | French             | French\_Male\_Speech\_New                    | Level-Headed Man          |
| 271 | French             | French\_Female\_News Anchor                  | Patient Female Presenter  |
| 272 | French             | French\_CasualMan                            | Casual Man                |
| 273 | French             | French\_MovieLeadFemale                      | Movie Lead Female         |
| 274 | French             | French\_FemaleAnchor                         | Female Anchor             |
| 275 | French             | French\_MaleNarrator                         | Male Narrator             |
| 276 | Indonesian         | Indonesian\_SweetGirl                        | Sweet Girl                |
| 277 | Indonesian         | Indonesian\_ReservedYoungMan                 | Reserved Young Man        |
| 278 | Indonesian         | Indonesian\_CharmingGirl                     | Charming Girl             |
| 279 | Indonesian         | Indonesian\_CalmWoman                        | Calm Woman                |
| 280 | Indonesian         | Indonesian\_ConfidentWoman                   | Confident Woman           |
| 281 | Indonesian         | Indonesian\_CaringMan                        | Caring Man                |
| 282 | Indonesian         | Indonesian\_BossyLeader                      | Bossy Leader              |
| 283 | Indonesian         | Indonesian\_DeterminedBoy                    | Determined Boy            |
| 284 | Indonesian         | Indonesian\_GentleGirl                       | Gentle Girl               |
| 285 | German             | German\_FriendlyMan                          | Friendly Man              |
| 286 | German             | German\_SweetLady                            | Sweet Lady                |
| 287 | German             | German\_PlayfulMan                           | Playful Man               |
| 288 | Russian            | Russian\_HandsomeChildhoodFriend             | Handsome Childhood Friend |
| 289 | Russian            | Russian\_BrightHeroine                       | Bright Queen              |
| 290 | Russian            | Russian\_AmbitiousWoman                      | Ambitious Woman           |
| 291 | Russian            | Russian\_ReliableMan                         | Reliable Man              |
| 292 | Russian            | Russian\_CrazyQueen                          | Crazy Girl                |
| 293 | Russian            | Russian\_PessimisticGirl                     | Pessimistic Girl          |
| 294 | Russian            | Russian\_AttractiveGuy                       | Attractive Guy            |
| 295 | Russian            | Russian\_Bad-temperedBoy                     | Bad-tempered Boy          |
| 296 | Italian            | Italian\_BraveHeroine                        | Brave Heroine             |
| 297 | Italian            | Italian\_Narrator                            | Narrator                  |
| 298 | Italian            | Italian\_WanderingSorcerer                   | Wandering Sorcerer        |
| 299 | Italian            | Italian\_DiligentLeader                      | Diligent Leader           |
| 300 | Dutch              | Dutch\_kindhearted\_girl                     | Kind-hearted girl         |
| 301 | Dutch              | Dutch\_bossy\_leader                         | Bossy leader              |
| 302 | Vietnamese         | Vietnamese\_kindhearted\_girl                | Kind-hearted girl         |
| 303 | Arabic             | Arabic\_CalmWoman                            | Calm Woman                |
| 304 | Arabic             | Arabic\_FriendlyGuy                          | Friendly Guy              |
| 305 | Turkish            | Turkish\_CalmWoman                           | Calm Woman                |
| 306 | Turkish            | Turkish\_Trustworthyman                      | Trustworthy man           |
| 307 | Ukrainian          | Ukrainian\_CalmWoman                         | Calm Woman                |
| 308 | Ukrainian          | Ukrainian\_WiseScholar                       | Wise Scholar              |
| 309 | Thai               | Thai\_male\_1\_sample8                       | Serene Man                |
| 310 | Thai               | Thai\_male\_2\_sample2                       | Friendly Man              |
| 311 | Thai               | Thai\_female\_1\_sample1                     | Confident Woman           |
| 312 | Thai               | Thai\_female\_2\_sample2                     | Energetic Woman           |
| 313 | Polish             | Polish\_male\_1\_sample4                     | Male Narrator             |
| 314 | Polish             | Polish\_male\_2\_sample3                     | Male Anchor               |
| 315 | Polish             | Polish\_female\_1\_sample1                   | Calm Woman                |
| 316 | Polish             | Polish\_female\_2\_sample3                   | Casual Woman              |
| 317 | Romanian           | Romanian\_male\_1\_sample2                   | Reliable Man              |
| 318 | Romanian           | Romanian\_male\_2\_sample1                   | Energetic Youth           |
| 319 | Romanian           | Romanian\_female\_1\_sample4                 | Optimistic Youth          |
| 320 | Romanian           | Romanian\_female\_2\_sample1                 | Gentle Woman              |
| 321 | Greek              | greek\_male\_1a\_v1                          | Thoughtful Mentor         |
| 322 | Greek              | Greek\_female\_1\_sample1                    | Gentle Lady               |
| 323 | Greek              | Greek\_female\_2\_sample3                    | Girl Next Door            |
| 324 | Czech              | czech\_male\_1\_v1                           | Assured Presenter         |
| 325 | Czech              | czech\_female\_5\_v7                         | Steadfast Narrator        |
| 326 | Czech              | czech\_female\_2\_v2                         | Elegant Lady              |
| 327 | Finnish            | finnish\_male\_3\_v1                         | Upbeat Man                |
| 328 | Finnish            | finnish\_male\_1\_v2                         | Friendly Boy              |
| 329 | Finnish            | finnish\_female\_4\_v1                       | Assetive Woman            |
| 330 | Hindi              | hindi\_male\_1\_v2                           | Trustworthy Advisor       |
| 331 | Hindi              | hindi\_female\_2\_v1                         | Tranquil Woman            |
| 332 | Hindi              | hindi\_female\_1\_v2                         | News Anchor               |

- Adjustable speech parameters:
  - Speed (0.5-2.0)
  - Volume (0-10)
  - Pitch (-12 to 12)

- Optional emotion settings:
  - Happy
  - Sad
  - Angry
  - Fearful
  - Disgusted
  - Surprised
  - Neutral
  - Fluent
  - Whisper

- Text normalization (Chinese/English)
  - Improves performance in digit-reading scenarios at the cost of slightly higher latency

## Add to HACS

1. Setup `HACS` https://hacs.xyz/docs/setup/prerequisites
2. In `Home Assistant`, click `HACS` on the menu on the left
3. Select `custom components`
4. Click the menu button in the top right hand corner
5. Choose `custom repositories`
6. Enter `https://github.com/thematrixdev/home-assistant-hailuo-ai-tts` and choose `Integration`, click `ADD`
7. Find and click on `Hailuo-AI TTS` in the `custom repositories` list
8. Click the `DOWNLOAD` button in the bottom right hand corner
9. Restart Home Assistant

## Install

1. Go to `Settings`, `Devices and Services`
2. Click the `Add Integration` button
3. Search `Hailuo-AI TTS`
4. Go through the configuration flow:

## Debug

- Add these lines to `configuration.yaml`

```yaml
logger:
  logs:
    custom_components.hailuo_ai_tts: debug
```

- Restart Home Assistant
- On Home Assistant, go to `Settings` -> `Logs`
- Click the `Show RAW logs` button
- Search `hailuo_ai_tts`

## Support

- Open an issue on GitHub
- Specify:
    - What's wrong
    - Home Assistant version
    - Hailuo-AI TTS custom-component version
    - Configuration (without sensitive data)
    - Logs

## Unofficial support

- Telegram Group https://t.me/smarthomehk

## Tested on

- Home Assistant Container 2025.12.4
