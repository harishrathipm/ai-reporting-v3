import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import PlainTextRenderer from './PlainTextRenderer';

describe('PlainTextRenderer', () => {
  it('renders plain text correctly', () => {
    const text = 'This is a plain text message.';

    render(<PlainTextRenderer text={text} />);

    expect(screen.getByText(text)).toBeInTheDocument();
  });
});
