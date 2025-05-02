import React from 'react';
import PropTypes from 'prop-types';
import log from 'loglevel';
import PaginatedTable from './PaginatedTable';
import ImageRenderer from './ImageRenderer';
import PlainTextRenderer from './PlainTextRenderer';
import ChartRenderer from './ChartRenderer';
import ErrorMessage from './ErrorMessage';
import LoadingSpinner from './LoadingSpinner';
import CardRenderer from './CardRenderer';

const ResponseRenderer = ({ response }) => {
  log.info('Rendering response:', response); // Log the response being rendered

  if (!response) return <LoadingSpinner />;

  switch (response.type) {
    case 'table':
      return <PaginatedTable columns={response.columns} rows={response.rows} />;
    case 'image':
      return <ImageRenderer src={response.src} alt={response.alt} />;
    case 'text':
      return <PlainTextRenderer text={response.data.response} />;
    case 'chart':
      return (
        <ChartRenderer
          type={response.chartType}
          data={response.data}
          options={response.options}
        />
      );
    case 'card':
      return <CardRenderer title={response.title} content={response.content} />;
    case 'error':
      return <ErrorMessage message={response.message} />;
    default:
      return <PlainTextRenderer text='Unsupported response type.' />;
  }
};

ResponseRenderer.propTypes = {
  response: PropTypes.shape({
    type: PropTypes.string.isRequired,
    columns: PropTypes.array,
    rows: PropTypes.array,
    src: PropTypes.string,
    alt: PropTypes.string,
    text: PropTypes.string,
    chartType: PropTypes.string,
    data: PropTypes.object,
    options: PropTypes.object,
    title: PropTypes.string,
    content: PropTypes.string,
    message: PropTypes.string,
  }),
};

export default ResponseRenderer;
