import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import { CssBaseline } from '@mui/material';
import Chat from './components/Chat';

function App() {
  return (
    <>
      <CssBaseline />
      <Router>
        <Routes>
          <Route path='/' element={<Chat />} />
          {/* Add more routes here as needed */}
        </Routes>
      </Router>
    </>
  );
}

export default App;
