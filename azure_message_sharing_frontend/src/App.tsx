import './App.css'
import { Route, Routes } from 'react-router-dom'
import AppIndex from './Index'

function App() {
  return (
      <Routes>
        <Route path='/' element={<AppIndex />} />
      </Routes>
  )
}

export default App
