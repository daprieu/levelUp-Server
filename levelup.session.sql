                SELECT
                    e.id,
                    e.date,
                    e.time,
                    e.description,
                    ge.gamer_id attendee,
                    e.game_id,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM
                    levelupapi_event e
                JOIN
                    levelupapi_gamer gr ON e.organizer_id = gr.id
                JOIN
                    levelupapi_gameevent ge ON e.id = ge.event_id
                JOIN
                    auth_user u ON gr.user_id = u.id