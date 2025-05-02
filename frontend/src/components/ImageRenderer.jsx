import React from 'react';
import { Box } from '@mui/material';
import PropTypes from 'prop-types';

const ImageRenderer = ({ src, alt }) => (
  <Box
    sx={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100%',
    }}
  >
    <img src={src} alt={alt} style={{ maxWidth: '100%', maxHeight: '100%' }} />
  </Box>
);

ImageRenderer.propTypes = {
  src: PropTypes.string.isRequired,
  alt: PropTypes.string.isRequired,
};

export default ImageRenderer;
