import React from 'react';
import { Typography } from '@mui/material';
import PropTypes from 'prop-types';

const PlainTextRenderer = ({ text }) => (
  <Typography variant='body1' sx={{ whiteSpace: 'pre-wrap' }}>
    {text}
  </Typography>
);

PlainTextRenderer.propTypes = {
  text: PropTypes.string.isRequired,
};

export default PlainTextRenderer;
