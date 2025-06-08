
import React from 'react';

interface MetricCardProps {
  title: string;
  value: number;
  icon: React.ReactNode;
  unit?: string;
}

const MetricCard = ({ title, value, icon, unit }: MetricCardProps) => {
  return (
    <div className="bg-white rounded-lg shadow p-8 border border-gray-200">
      <div className="flex items-center justify-between">
        <div>
          <h3 className="text-base font-medium text-gray-600">{title}</h3>
          <p className="text-3xl font-bold text-gray-900 mt-2">
            {value}
            {unit && <span className="text-lg font-normal text-gray-500 ml-1">{unit}</span>}
          </p>
        </div>
        <div className="text-blue-600">
          {icon}
        </div>
      </div>
    </div>
  );
};

export default MetricCard;
