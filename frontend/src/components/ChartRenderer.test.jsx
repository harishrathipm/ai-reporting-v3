import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import ChartRenderer from './ChartRenderer';

describe('ChartRenderer', () => {
  it('renders a bar chart correctly', () => {
    const data = {
      labels: ['January', 'February', 'March'],
      datasets: [
        {
          label: 'Sales',
          data: [65, 59, 80],
          backgroundColor: ['rgba(75, 192, 192, 0.2)'],
          borderColor: ['rgba(75, 192, 192, 1)'],
          borderWidth: 1,
        },
      ],
    };

    const options = { responsive: true };

    const { container } = render(
      <ChartRenderer type='bar' data={data} options={options} />
    );
    expect(container).toBeInTheDocument();
  });
});
