import React from 'react';
import { Box, Typography } from '@mui/material';

const MessageBubble = ({ text, sender }) => (
  <Box
    sx={{
      display: 'flex',
      justifyContent: sender === 'user' ? 'flex-end' : 'flex-start',
      marginBottom: 1,
    }}
  >
    <Typography
      sx={{
        padding: 1,
        borderRadius: 1,
        backgroundColor: sender === 'user' ? '#007bff' : '#f1f1f1',
        color: sender === 'user' ? '#fff' : '#333',
        maxWidth: '70%',
        wordWrap: 'break-word',
      }}
    >
      {text}
    </Typography>
  </Box>
);

export default MessageBubble;
