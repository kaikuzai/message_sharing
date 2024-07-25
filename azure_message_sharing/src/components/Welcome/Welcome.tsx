import React from 'react'
import useWelcome from '../../hooks/useWelcome'

const Welcome = () => {

    const {data} = useWelcome()

    console.log("This is the data dot reply", data?.reply)
  return (
    <div>
        <h1>
        {data?.reply || 'nothing'}
        </h1>
    </div>
  )
}

export default Welcome