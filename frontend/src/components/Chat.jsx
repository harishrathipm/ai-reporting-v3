import React, { useState } from 'react';
import { Box, TextField, Button, Typography, Paper } from '@mui/material';
import ChatAPI from '../api/ChatAPI';
import MessageBubble from './MessageBubble';
import ResponseRenderer from './ResponseRenderer';

function Chat() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: 'user', text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput('');

    try {
      const data = await ChatAPI.sendMessage(input);
      const botMessage = { sender: 'bot', response: data };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Error:', error);
      const errorMessage = {
        sender: 'bot',
        response: {
          type: 'error',
          message: 'Failed to fetch response. Please try again.',
        },
      };
      setMessages((prev) => [...prev, errorMessage]);
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        height: '100vh',
        width: '100vw',
        backgroundColor: '#f4f4f9',
      }}
    >
      <Paper
        elevation={3}
        sx={{
          flex: 1,
          margin: 2,
          padding: 2,
          display: 'flex',
          flexDirection: 'column',
          gap: 2,
          overflow: 'hidden',
        }}
      >
        <Box
          sx={{
            flex: 1,
            overflowY: 'auto',
            padding: 1,
            display: 'flex',
            flexDirection: 'column',
            gap: 1,
          }}
        >
          {console.log('Messages:', messages)}
          {messages.map((msg, index) =>
            msg.sender === 'user' ? (
              <MessageBubble key={index} text={msg.text} sender={msg.sender} />
            ) : (
              <ResponseRenderer key={index} response={msg.response} />
            )
          )}
        </Box>
        <Box sx={{ display: 'flex', gap: 1 }}>
          <TextField
            fullWidth
            variant='outlined'
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder='Type your message...'
          />
          <Button variant='contained' color='primary' onClick={sendMessage}>
            Send
          </Button>
        </Box>
      </Paper>
    </Box>
  );
}

export default Chat;
