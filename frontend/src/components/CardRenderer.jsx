import React from 'react';
import { Card, CardContent, Typography } from '@mui/material';
import PropTypes from 'prop-types';

const CardRenderer = ({ title, content }) => (
  <Card sx={{ margin: 2 }}>
    <CardContent>
      <Typography variant='h5' component='div'>
        {title}
      </Typography>
      <Typography variant='body2' color='text.secondary'>
        {content}
      </Typography>
    </CardContent>
  </Card>
);

CardRenderer.propTypes = {
  title: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
};

export default CardRenderer;
