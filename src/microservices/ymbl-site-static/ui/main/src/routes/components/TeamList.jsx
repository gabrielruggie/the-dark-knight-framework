import React from 'react';
import Team from './Team';

export default function TeamList({teamMap}) {

    return (
        teamMap.map(
            team => <Team Team={team} />
        )
    )
}