import React, { useState } from 'react';
import Header from './Header';
import MetricCard from './MetricCard';
import ChartSection from './ChartSection';
import RightPanel from './RightPanel';
import { Thermometer, Droplets, Gauge, Zap } from 'lucide-react';
import { generateRandomData } from '../utils/dataGenerator';
import { Card } from './ui/card';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from './ui/select';

const mockData = {
  temperature: [
    { time: 'T1', value: 20 },
    { time: 'T2', value: 22 },
    { time: 'T3', value: 25 },
    { time: 'T4', value: 21 },
    { time: 'T5', value: 23 },
    { time: 'T6', value: 24 },
  ],
  humidity: [
    { time: 'T1', value: 40 },
    { time: 'T2', value: 45 },
    { time: 'T3', value: 42 },
    { time: 'T4', value: 48 },
    { time: 'T5', value: 44 },
    { time: 'T6', value: 46 },
  ],
};

const Dashboard = () => {
  const [isLiveData, setIsLiveData] = useState(false);
  const [chartTypes, setChartTypes] = useState({
    temperature: 'line',
    humidity: 'bar', 
    pressure: 'radar',
    vibration: 'area'
  });
  const [metrics] = useState(generateRandomData().metrics);

  const handleLiveDataToggle = () => {
    setIsLiveData(!isLiveData);
  };

  const handleChartTypeChange = (metric: string, type: string) => {
    setChartTypes(prev => ({
      ...prev,
      [metric]: type
    }));
  };

  return (
    <div className="p-6 max-w-7xl mx-auto">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Mounting 2 Dashboard</h1>
        <div className="flex gap-4">
          <Select defaultValue="7days">
            <SelectTrigger className="w-[180px]">
              <SelectValue placeholder="Select time range" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="7days">Last 7 days</SelectItem>
              <SelectItem value="30days">Last 30 days</SelectItem>
              <SelectItem value="90days">Last 90 days</SelectItem>
            </SelectContent>
          </Select>
          <button className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700">
            Refresh
          </button>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        <MetricCard
          title="Temperature"
          value={12}
          unit="°C"
          icon={<span className="text-red-500">🌡️</span>}
        />
        <MetricCard
          title="Humidity"
          value={24}
          unit="%"
          icon={<span className="text-blue-500">💧</span>}
        />
        <MetricCard
          title="Pressure"
          value={17}
          unit="Bar"
          icon={<span className="text-green-500">📊</span>}
        />
        <MetricCard
          title="Energy"
          value={78}
          unit="J"
          icon={<span className="text-yellow-500">⚡</span>}
        />
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card className="p-4">
          <h3 className="text-lg font-medium mb-4">Temperature (°C)</h3>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={mockData.temperature}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="time" />
                <YAxis />
                <Tooltip />
                <Line
                  type="monotone"
                  dataKey="value"
                  stroke="#2563eb"
                  strokeWidth={2}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </Card>

        <Card className="p-4">
          <h3 className="text-lg font-medium mb-4">Humidity (%)</h3>
          <div className="h-[300px]">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={mockData.humidity}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="time" />
                <YAxis />
                <Tooltip />
                <Line
                  type="monotone"
                  dataKey="value"
                  stroke="#0891b2"
                  strokeWidth={2}
                />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;
