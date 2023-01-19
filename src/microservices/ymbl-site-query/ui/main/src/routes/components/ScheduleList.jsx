import React from 'react';
import ScheduledGame from './ScheduledGame';

export default function ScheduleList({games}) {

    return (
        games.map(
            game => <ScheduledGame game={game} />
        )
    )
}