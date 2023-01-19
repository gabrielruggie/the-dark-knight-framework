import React, {useState} from 'react';
import StandingsTeam from './StandingsTeam';

export default function StandingsTeamList({standingTeams}) {

    return (
        standingTeams.map(
            team => <StandingsTeam team={team} />
        )
    )
}