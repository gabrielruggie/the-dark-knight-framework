import React from 'react';
import Player from './Player';

export default function PlayerList({teamPlayers}) {

    return (
        teamPlayers.map(
            player => <Player player={player}/>
        )
    )
}