import React from 'react';
import { Box } from '@mui/material';
import PropTypes from 'prop-types';
import { Bar, Line, Pie } from 'react-chartjs-2';

const ChartRenderer = ({ type, data, options }) => {
  const renderChart = () => {
    switch (type) {
      case 'bar':
        return <Bar data={data} options={options} />;
      case 'line':
        return <Line data={data} options={options} />;
      case 'pie':
        return <Pie data={data} options={options} />;
      default:
        return null;
    }
  };

  return <Box>{renderChart()}</Box>;
};

ChartRenderer.propTypes = {
  type: PropTypes.oneOf(['bar', 'line', 'pie']).isRequired,
  data: PropTypes.object.isRequired,
  options: PropTypes.object,
};

export default ChartRenderer;
