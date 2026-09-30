library(dplyr)

df = read.csv('people.csv')

df = df |> mutate(position=ifelse(alumni=='', position, ''),
                  team=ifelse(alumni=='', team, ''),
                  position_en=ifelse(alumni=='', position_en, ''))

colnames(df)

df = df |> select(id, first_name, last_name, email, team, position, position_en,
                  phone, room, subteam,
                  oa_id, selected_dois,
                  alumni, alumni_position, alumni_position_en)

df$selected_dois = ''

write.csv(df, file='people.csv', quote=FALSE, row.names=FALSE)
